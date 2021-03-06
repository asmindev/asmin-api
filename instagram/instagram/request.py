from dataclasses import dataclass
from typing import Text, Dict
import time
import requests
from .endpoints import endpoints

instagram = endpoints()


@dataclass
class Session:
    FULLNAME: Text = ""
    USER_ID: int = 0
    USERNAME: Text = ""
    PROFILE_PIC_URL: Text = ""
    IS_VERIFIED: bool = False
    IS_PRIVATE: bool = False
    FOLLOWING: int = 0
    FOLLOWERS: int = 0

    def __init__(self, user_agent: Text = None):
        """
        user_agent: user agent to use for this session
        """
        self.requests = requests.Session()
        self.__is_logged: bool = False
        self.__use_cookie: bool = False
        self.__use_password: bool = False
        self.__username: Text = ""
        self.__password: Text = ""
        self.__cookie: Text = ""
        self.__user_agent: Text = (
            user_agent if user_agent is not None else instagram.USER_AGENT
        )

    def login(self):
        if self.__use_password:
            response = self.requests.get(instagram.BASE_URL)
            csrf = instagram.csrftoken(response.text)
            mid = self.requests.get(instagram.MID).text
            self.requests.headers.update(
                {
                    "cookie": f"ig_pr=2;ig_cb=1;csrftoken={csrf};mid={mid};",
                    "x-csrftoken": csrf,
                }
            )
            payload = {
                "username": self.__username,
                "enc_password": "#PWD_INSTAGRAM_BROWSER"
                f":0:{int(time.time())}:{self.__password}",
            }
            login = self.requests.post(
                instagram.LOGIN_URL, data=payload, allow_redirects=True
            )
            if login.status_code == 200:
                csrftoken = login.cookies.get("csrftoken")
                if csrftoken:
                    login.cookies.update(dict(mid=mid))
                    self.requests.headers.update({"x-csrftoken": csrftoken})
                    cookie = ";".join(
                        [
                            f"{key}={value}"
                            for key, value in login.cookies.get_dict().items()
                        ]
                    )
                    self.__cookie = cookie
                    self.requests.headers.update(dict(cookie=self.__cookie))
                    response = login.json()
                    if response["authenticated"]:
                        self.__is_logged = True
                resp: Dict = login.json()
                resp.update(dict(cookie=self.__cookie))
                return resp
            else:
                return dict(
                    status_code=login.status_code,
                    messages="uknown error",
                )
        elif self.__use_cookie:
            response = self.requests.get(instagram.BASE_URL)
            if "prefill_phone_number" not in response.text:
                self.__is_logged = True
                return dict(success=True)
            else:
                return dict(success=False)
        else:
            raise ValueError("You has to set method login")

    @property
    def is_logged(self):
        return self.__is_logged

    @property
    def cookies(self):
        return "set cookies", 1

    @cookies.setter
    def set_cookies(self, cookies: Text):
        if not self.__use_password:
            if "csrftoken" not in cookies.lower():
                raise ValueError(f"invalid cookies: {cookies}")
            else:
                if not self.__is_logged:
                    self.__use_cookie = True
                    self.__cookie = cookies
                    data = {
                        x[0]: x[1]
                        for x in list(
                            map(
                                lambda cookie: cookie.split("="),
                                cookies.replace(" ", "").split(";"),
                            )
                        )
                    }
                    self.requests.cookies.update(data)
                    self.requests.headers.update(
                        {
                            "x-csrftoken": data["csrftoken"],
                            "cookie": self.__cookie,
                            "User-Agent": self.__user_agent,
                        }
                    )
                else:
                    raise ValueError("You has logged")
        else:
            raise ValueError("You has login use password")
        return self.__cookie

    def set_credentials(self, username: Text, password: Text):
        if not self.__use_cookie:
            if not self.__is_logged:
                self.__use_password = True
                self.__username = username
                self.__password = password
                self.requests.headers.update(
                    {
                        "User-Agent": self.__user_agent,
                    }
                )
                return "credentials setting up"
            else:
                raise ValueError("You has logged")

        else:
            raise ValueError("You has been login use cookie")

    def set_headers(self, **kwargs):
        self.requests.headers.update(kwargs)
