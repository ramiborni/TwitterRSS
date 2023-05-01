from enum import Enum
from dataclasses import dataclass
from typing import Optional, Any, List, TypeVar, Type, cast, Callable


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def is_type(t: Type[T], x: Any) -> T:
    assert isinstance(x, t)
    return x


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


class CursorType(Enum):
    BOTTOM = "Bottom"
    TOP = "Top"


class EntryTypeEnum(Enum):
    TIMELINE_TIMELINE_CURSOR = "TimelineTimelineCursor"
    TIMELINE_TIMELINE_ITEM = "TimelineTimelineItem"


class ItemTypeEnum(Enum):
    TIMELINE_TWEET = "TimelineTweet"


class TweetDisplayType(Enum):
    TWEET = "Tweet"


@dataclass
class RGB:
    blue: Optional[int] = None
    green: Optional[int] = None
    red: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'RGB':
        assert isinstance(obj, dict)
        blue = from_union([from_int, from_none], obj.get("blue"))
        green = from_union([from_int, from_none], obj.get("green"))
        red = from_union([from_int, from_none], obj.get("red"))
        return RGB(blue, green, red)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.blue is not None:
            result["blue"] = from_union([from_int, from_none], self.blue)
        if self.green is not None:
            result["green"] = from_union([from_int, from_none], self.green)
        if self.red is not None:
            result["red"] = from_union([from_int, from_none], self.red)
        return result


@dataclass
class Palette:
    rgb: Optional[RGB] = None
    percentage: Optional[float] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Palette':
        assert isinstance(obj, dict)
        rgb = from_union([RGB.from_dict, from_none], obj.get("rgb"))
        percentage = from_union([from_float, from_none], obj.get("percentage"))
        return Palette(rgb, percentage)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.rgb is not None:
            result["rgb"] = from_union([lambda x: to_class(RGB, x), from_none], self.rgb)
        if self.percentage is not None:
            result["percentage"] = from_union([to_float, from_none], self.percentage)
        return result


@dataclass
class ImageColorValue:
    palette: Optional[List[Palette]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ImageColorValue':
        assert isinstance(obj, dict)
        palette = from_union([lambda x: from_list(Palette.from_dict, x), from_none], obj.get("palette"))
        return ImageColorValue(palette)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.palette is not None:
            result["palette"] = from_union([lambda x: from_list(lambda x: to_class(Palette, x), x), from_none], self.palette)
        return result


@dataclass
class ImageValue:
    height: Optional[int] = None
    width: Optional[int] = None
    url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ImageValue':
        assert isinstance(obj, dict)
        height = from_union([from_int, from_none], obj.get("height"))
        width = from_union([from_int, from_none], obj.get("width"))
        url = from_union([from_str, from_none], obj.get("url"))
        return ImageValue(height, width, url)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.height is not None:
            result["height"] = from_union([from_int, from_none], self.height)
        if self.width is not None:
            result["width"] = from_union([from_int, from_none], self.width)
        if self.url is not None:
            result["url"] = from_union([from_str, from_none], self.url)
        return result


class ValueType(Enum):
    IMAGE = "IMAGE"
    IMAGE_COLOR = "IMAGE_COLOR"
    STRING = "STRING"
    USER = "USER"


@dataclass
class UserValue:
    id_str: Optional[int] = None
    path: Optional[List[Any]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'UserValue':
        assert isinstance(obj, dict)
        id_str = from_union([from_none, lambda x: int(from_str(x))], obj.get("id_str"))
        path = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("path"))
        return UserValue(id_str, path)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.id_str is not None:
            result["id_str"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.id_str)
        if self.path is not None:
            result["path"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.path)
        return result


@dataclass
class Value:
    string_value: Optional[str] = None
    type: Optional[ValueType] = None
    scribe_key: Optional[str] = None
    image_value: Optional[ImageValue] = None
    image_color_value: Optional[ImageColorValue] = None
    user_value: Optional[UserValue] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Value':
        assert isinstance(obj, dict)
        string_value = from_union([from_str, from_none], obj.get("string_value"))
        type = from_union([ValueType, from_none], obj.get("type"))
        scribe_key = from_union([from_str, from_none], obj.get("scribe_key"))
        image_value = from_union([ImageValue.from_dict, from_none], obj.get("image_value"))
        image_color_value = from_union([ImageColorValue.from_dict, from_none], obj.get("image_color_value"))
        user_value = from_union([UserValue.from_dict, from_none], obj.get("user_value"))
        return Value(string_value, type, scribe_key, image_value, image_color_value, user_value)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.string_value is not None:
            result["string_value"] = from_union([from_str, from_none], self.string_value)
        if self.type is not None:
            result["type"] = from_union([lambda x: to_enum(ValueType, x), from_none], self.type)
        if self.scribe_key is not None:
            result["scribe_key"] = from_union([from_str, from_none], self.scribe_key)
        if self.image_value is not None:
            result["image_value"] = from_union([lambda x: to_class(ImageValue, x), from_none], self.image_value)
        if self.image_color_value is not None:
            result["image_color_value"] = from_union([lambda x: to_class(ImageColorValue, x), from_none], self.image_color_value)
        if self.user_value is not None:
            result["user_value"] = from_union([lambda x: to_class(UserValue, x), from_none], self.user_value)
        return result


@dataclass
class BindingValue:
    key: Optional[str] = None
    value: Optional[Value] = None

    @staticmethod
    def from_dict(obj: Any) -> 'BindingValue':
        assert isinstance(obj, dict)
        key = from_union([from_str, from_none], obj.get("key"))
        value = from_union([Value.from_dict, from_none], obj.get("value"))
        return BindingValue(key, value)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.key is not None:
            result["key"] = from_union([from_str, from_none], self.key)
        if self.value is not None:
            result["value"] = from_union([lambda x: to_class(Value, x), from_none], self.value)
        return result


@dataclass
class Audience:
    name: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Audience':
        assert isinstance(obj, dict)
        name = from_union([from_str, from_none], obj.get("name"))
        return Audience(name)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        return result


@dataclass
class Device:
    version: Optional[int] = None
    name: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Device':
        assert isinstance(obj, dict)
        version = from_union([from_none, lambda x: int(from_str(x))], obj.get("version"))
        name = from_union([from_str, from_none], obj.get("name"))
        return Device(version, name)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.version is not None:
            result["version"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.version)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        return result


@dataclass
class Platform:
    audience: Optional[Audience] = None
    device: Optional[Device] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Platform':
        assert isinstance(obj, dict)
        audience = from_union([Audience.from_dict, from_none], obj.get("audience"))
        device = from_union([Device.from_dict, from_none], obj.get("device"))
        return Platform(audience, device)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.audience is not None:
            result["audience"] = from_union([lambda x: to_class(Audience, x), from_none], self.audience)
        if self.device is not None:
            result["device"] = from_union([lambda x: to_class(Device, x), from_none], self.device)
        return result


@dataclass
class CardPlatform:
    platform: Optional[Platform] = None

    @staticmethod
    def from_dict(obj: Any) -> 'CardPlatform':
        assert isinstance(obj, dict)
        platform = from_union([Platform.from_dict, from_none], obj.get("platform"))
        return CardPlatform(platform)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.platform is not None:
            result["platform"] = from_union([lambda x: to_class(Platform, x), from_none], self.platform)
        return result


@dataclass
class UnmentionData:
    pass

    @staticmethod
    def from_dict(obj: Any) -> 'UnmentionData':
        assert isinstance(obj, dict)
        return UnmentionData()

    def to_dict(self) -> dict:
        result: dict = {}
        return result


class ID(Enum):
    VX_NLCJO0_NZ_QZ_MZ_Q2_ND_YY = "VXNlcjo0NzQzMzQ2NDYy"
    VX_NLCJO3_MD_UZ_NZ_UX_MTQ4_MJK4_O_DK1_MZ_Y = "VXNlcjo3MDUzNzUxMTQ4Mjk4ODk1MzY="
    VX_NLCJO5_MT_YY_MTU2_M_TG2_MTI5_NZ_M1_NJG = "VXNlcjo5MTYyMTU2MTg2MTI5NzM1Njg="
    VX_NLCJO5_NZ_U2_NJ_Y4_O_DCX_NZ_M1_NJ_Y0_NJ_Q = "VXNlcjo5NzU2NjY4ODcxNzM1NjY0NjQ="
    VX_NLCJOX_MDA1_ODI2_ODM2 = "VXNlcjoxMDA1ODI2ODM2"
    VX_NLCJOX_MJ_Q4_ND_EX_OT_YW = "VXNlcjoxMjQ4NDExOTYw"
    VX_NLCJOX_MJ_UX_NTM4_NDE2 = "VXNlcjoxMjUxNTM4NDE2"
    VX_NLCJOX_NDY5_MZ_A4_MDA4 = "VXNlcjoxNDY5MzA4MDA4"
    VX_NLCJOY_MD_YY_O_TG1_OA = "VXNlcjoyMDYyOTg1OA=="
    VX_NLCJOY_M_TK3_NZ_AX_NDA1 = "VXNlcjoyMTk3NzAxNDA1"
    VX_NLCJOY_M_TKX_N_DC4_ODQ5 = "VXNlcjoyMTkxNDc4ODQ5"
    VX_NLCJOY_NJ_U5_MD_MZ_MDY = "VXNlcjoyNjU5MDMzMDY="
    VX_NLCJOY_NZG0_N_DC0_MG = "VXNlcjoyNzg0NDc0Mg=="


class CreatedAt(Enum):
    FRI_JAN_0809515600002016 = "Fri Jan 08 09:51:56 +0000 2016"
    FRI_MAR_0812053400002013 = "Fri Mar 08 12:05:34 +0000 2013"
    FRI_NOV_2215382100002013 = "Fri Nov 22 15:38:21 +0000 2013"
    FRI_OCT_0608164000002017 = "Fri Oct 06 08:16:40 +0000 2017"
    MON_MAR_1409462200002011 = "Mon Mar 14 09:46:22 +0000 2011"
    MON_MAR_1909344700002018 = "Mon Mar 19 09:34:47 +0000 2018"
    THU_MAR_0312514700002016 = "Thu Mar 03 12:51:47 +0000 2016"
    THU_MAR_0710285200002013 = "Thu Mar 07 10:28:52 +0000 2013"
    THU_MAY_3009213800002013 = "Thu May 30 09:21:38 +0000 2013"
    TUE_MAR_3110032700002009 = "Tue Mar 31 10:03:27 +0000 2009"
    WED_DEC_1207552000002012 = "Wed Dec 12 07:55:20 +0000 2012"
    WED_FEB_1121264400002009 = "Wed Feb 11 21:26:44 +0000 2009"
    WED_NOV_2709155500002013 = "Wed Nov 27 09:15:55 +0000 2013"


@dataclass
class URL:
    display_url: Optional[str] = None
    expanded_url: Optional[str] = None
    url: Optional[str] = None
    indices: Optional[List[int]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'URL':
        assert isinstance(obj, dict)
        display_url = from_union([from_str, from_none], obj.get("display_url"))
        expanded_url = from_union([from_str, from_none], obj.get("expanded_url"))
        url = from_union([from_str, from_none], obj.get("url"))
        indices = from_union([lambda x: from_list(from_int, x), from_none], obj.get("indices"))
        return URL(display_url, expanded_url, url, indices)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.display_url is not None:
            result["display_url"] = from_union([from_str, from_none], self.display_url)
        if self.expanded_url is not None:
            result["expanded_url"] = from_union([from_str, from_none], self.expanded_url)
        if self.url is not None:
            result["url"] = from_union([from_str, from_none], self.url)
        if self.indices is not None:
            result["indices"] = from_union([lambda x: from_list(from_int, x), from_none], self.indices)
        return result


@dataclass
class Description:
    urls: Optional[List[URL]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Description':
        assert isinstance(obj, dict)
        urls = from_union([lambda x: from_list(URL.from_dict, x), from_none], obj.get("urls"))
        return Description(urls)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.urls is not None:
            result["urls"] = from_union([lambda x: from_list(lambda x: to_class(URL, x), x), from_none], self.urls)
        return result


@dataclass
class PurpleEntities:
    description: Optional[Description] = None
    url: Optional[Description] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PurpleEntities':
        assert isinstance(obj, dict)
        description = from_union([Description.from_dict, from_none], obj.get("description"))
        url = from_union([Description.from_dict, from_none], obj.get("url"))
        return PurpleEntities(description, url)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.description is not None:
            result["description"] = from_union([lambda x: to_class(Description, x), from_none], self.description)
        if self.url is not None:
            result["url"] = from_union([lambda x: to_class(Description, x), from_none], self.url)
        return result


class Location(Enum):
    BERGEN_NORGE = "Bergen, Norge"
    EMPTY = ""
    MONS_NORWAY = "Mons, Norway"
    MØRE_OG_ROMSDAL_NORGE = "Møre og Romsdal, Norge"
    NORGE = "Norge"
    OSLO = "Oslo"
    PORSGRUNN_NORGE = "Porsgrunn, Norge"
    ROGALAND_BRANN_OG_REDNING_IKS = "Rogaland brann og redning IKS"
    TROMSØ_NORWAY = "Tromsø, Norway"
    VESTLAND_FYLKE = "Vestland fylke"


class Name(Enum):
    BARENTS_WATCH = "BarentsWatch"
    HRS_SØR_NORGE = "HRS Sør-Norge"
    METEOROLOGENE = "Meteorologene"
    NRK_TRAFIKK = "NRK Trafikk"
    POLITIET_I_SØR_VEST = "Politiet i Sør-Vest"
    POLITIET_MØRE_ROMSDAL = "Politiet MøreRomsdal"
    STATENS_VEGVESEN = "Statens vegvesen"
    SØR_ØST_POLITIDISTRIKT = "Sør-Øst politidistrikt"
    THE_110_SØR_VEST = "110 Sør-Vest"
    THE_110_VEST = "110 Vest"
    VEGTRAFIKKSENTRALEN_SØR = "Vegtrafikksentralen sør"
    VEGTRAFIKKSENTRALEN_VEST = "Vegtrafikksentralen vest"
    VEST_POLITIDISTRIKT = "Vest politidistrikt"


class ScreenName(Enum):
    BARENTS_WATCH = "BarentsWatch"
    HAAVARDBERGEN = "haavardbergen"
    HRS_SOR_NORGE = "HRSSorNorge"
    KENTEINAR = "kenteinar"
    METEOROLOGENE = "Meteorologene"
    NRK_TRAFIKK = "NRKTrafikk"
    POLITIETSOROST = "politietsorost"
    POLITIETSORVEST = "politietsorvest"
    POLITIVEST = "politivest"
    POLITI_M_RPD = "PolitiMRpd"
    PRESSEROM = "Presserom"
    THE_110_SOR_VEST = "110SorVest"
    THE_110_VEST = "110Vest"
    VTS_SOR = "VTS_sor"
    VT_SVEST = "VTSvest"


class TranslatorType(Enum):
    NONE = "none"


@dataclass
class PurpleLegacy:
    created_at: Optional[CreatedAt] = None
    default_profile: Optional[bool] = None
    default_profile_image: Optional[bool] = None
    description: Optional[str] = None
    entities: Optional[PurpleEntities] = None
    fast_followers_count: Optional[int] = None
    favourites_count: Optional[int] = None
    followers_count: Optional[int] = None
    friends_count: Optional[int] = None
    has_custom_timelines: Optional[bool] = None
    is_translator: Optional[bool] = None
    listed_count: Optional[int] = None
    location: Optional[Location] = None
    media_count: Optional[int] = None
    name: Optional[Name] = None
    normal_followers_count: Optional[int] = None
    pinned_tweet_ids_str: Optional[List[str]] = None
    possibly_sensitive: Optional[bool] = None
    profile_banner_url: Optional[str] = None
    profile_image_url_https: Optional[str] = None
    profile_interstitial_type: Optional[str] = None
    screen_name: Optional[ScreenName] = None
    statuses_count: Optional[int] = None
    translator_type: Optional[TranslatorType] = None
    url: Optional[str] = None
    verified: Optional[bool] = None
    withheld_in_countries: Optional[List[Any]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PurpleLegacy':
        assert isinstance(obj, dict)
        created_at = from_union([CreatedAt, from_none], obj.get("created_at"))
        default_profile = from_union([from_bool, from_none], obj.get("default_profile"))
        default_profile_image = from_union([from_bool, from_none], obj.get("default_profile_image"))
        description = from_union([from_str, from_none], obj.get("description"))
        entities = from_union([PurpleEntities.from_dict, from_none], obj.get("entities"))
        fast_followers_count = from_union([from_int, from_none], obj.get("fast_followers_count"))
        favourites_count = from_union([from_int, from_none], obj.get("favourites_count"))
        followers_count = from_union([from_int, from_none], obj.get("followers_count"))
        friends_count = from_union([from_int, from_none], obj.get("friends_count"))
        has_custom_timelines = from_union([from_bool, from_none], obj.get("has_custom_timelines"))
        is_translator = from_union([from_bool, from_none], obj.get("is_translator"))
        listed_count = from_union([from_int, from_none], obj.get("listed_count"))
        location = from_union([Location, from_none], obj.get("location"))
        media_count = from_union([from_int, from_none], obj.get("media_count"))
        name = from_union([Name, from_none], obj.get("name"))
        normal_followers_count = from_union([from_int, from_none], obj.get("normal_followers_count"))
        pinned_tweet_ids_str = from_union([lambda x: from_list(from_str, x), from_none], obj.get("pinned_tweet_ids_str"))
        possibly_sensitive = from_union([from_bool, from_none], obj.get("possibly_sensitive"))
        profile_banner_url = from_union([from_str, from_none], obj.get("profile_banner_url"))
        profile_image_url_https = from_union([from_str, from_none], obj.get("profile_image_url_https"))
        profile_interstitial_type = from_union([from_str, from_none], obj.get("profile_interstitial_type"))
        screen_name = from_union([ScreenName, from_none], obj.get("screen_name"))
        statuses_count = from_union([from_int, from_none], obj.get("statuses_count"))
        translator_type = from_union([TranslatorType, from_none], obj.get("translator_type"))
        url = from_union([from_str, from_none], obj.get("url"))
        verified = from_union([from_bool, from_none], obj.get("verified"))
        withheld_in_countries = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("withheld_in_countries"))
        return PurpleLegacy(created_at, default_profile, default_profile_image, description, entities, fast_followers_count, favourites_count, followers_count, friends_count, has_custom_timelines, is_translator, listed_count, location, media_count, name, normal_followers_count, pinned_tweet_ids_str, possibly_sensitive, profile_banner_url, profile_image_url_https, profile_interstitial_type, screen_name, statuses_count, translator_type, url, verified, withheld_in_countries)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.created_at is not None:
            result["created_at"] = from_union([lambda x: to_enum(CreatedAt, x), from_none], self.created_at)
        if self.default_profile is not None:
            result["default_profile"] = from_union([from_bool, from_none], self.default_profile)
        if self.default_profile_image is not None:
            result["default_profile_image"] = from_union([from_bool, from_none], self.default_profile_image)
        if self.description is not None:
            result["description"] = from_union([from_str, from_none], self.description)
        if self.entities is not None:
            result["entities"] = from_union([lambda x: to_class(PurpleEntities, x), from_none], self.entities)
        if self.fast_followers_count is not None:
            result["fast_followers_count"] = from_union([from_int, from_none], self.fast_followers_count)
        if self.favourites_count is not None:
            result["favourites_count"] = from_union([from_int, from_none], self.favourites_count)
        if self.followers_count is not None:
            result["followers_count"] = from_union([from_int, from_none], self.followers_count)
        if self.friends_count is not None:
            result["friends_count"] = from_union([from_int, from_none], self.friends_count)
        if self.has_custom_timelines is not None:
            result["has_custom_timelines"] = from_union([from_bool, from_none], self.has_custom_timelines)
        if self.is_translator is not None:
            result["is_translator"] = from_union([from_bool, from_none], self.is_translator)
        if self.listed_count is not None:
            result["listed_count"] = from_union([from_int, from_none], self.listed_count)
        if self.location is not None:
            result["location"] = from_union([lambda x: to_enum(Location, x), from_none], self.location)
        if self.media_count is not None:
            result["media_count"] = from_union([from_int, from_none], self.media_count)
        if self.name is not None:
            result["name"] = from_union([lambda x: to_enum(Name, x), from_none], self.name)
        if self.normal_followers_count is not None:
            result["normal_followers_count"] = from_union([from_int, from_none], self.normal_followers_count)
        if self.pinned_tweet_ids_str is not None:
            result["pinned_tweet_ids_str"] = from_union([lambda x: from_list(from_str, x), from_none], self.pinned_tweet_ids_str)
        if self.possibly_sensitive is not None:
            result["possibly_sensitive"] = from_union([from_bool, from_none], self.possibly_sensitive)
        if self.profile_banner_url is not None:
            result["profile_banner_url"] = from_union([from_str, from_none], self.profile_banner_url)
        if self.profile_image_url_https is not None:
            result["profile_image_url_https"] = from_union([from_str, from_none], self.profile_image_url_https)
        if self.profile_interstitial_type is not None:
            result["profile_interstitial_type"] = from_union([from_str, from_none], self.profile_interstitial_type)
        if self.screen_name is not None:
            result["screen_name"] = from_union([lambda x: to_enum(ScreenName, x), from_none], self.screen_name)
        if self.statuses_count is not None:
            result["statuses_count"] = from_union([from_int, from_none], self.statuses_count)
        if self.translator_type is not None:
            result["translator_type"] = from_union([lambda x: to_enum(TranslatorType, x), from_none], self.translator_type)
        if self.url is not None:
            result["url"] = from_union([from_str, from_none], self.url)
        if self.verified is not None:
            result["verified"] = from_union([from_bool, from_none], self.verified)
        if self.withheld_in_countries is not None:
            result["withheld_in_countries"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.withheld_in_countries)
        return result


@dataclass
class Category:
    id: Optional[int] = None
    name: Optional[str] = None
    icon_name: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Category':
        assert isinstance(obj, dict)
        id = from_union([from_int, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        icon_name = from_union([from_str, from_none], obj.get("icon_name"))
        return Category(id, name, icon_name)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.id is not None:
            result["id"] = from_union([from_int, from_none], self.id)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.icon_name is not None:
            result["icon_name"] = from_union([from_str, from_none], self.icon_name)
        return result


@dataclass
class Professional:
    rest_id: Optional[str] = None
    professional_type: Optional[str] = None
    category: Optional[List[Category]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Professional':
        assert isinstance(obj, dict)
        rest_id = from_union([from_str, from_none], obj.get("rest_id"))
        professional_type = from_union([from_str, from_none], obj.get("professional_type"))
        category = from_union([lambda x: from_list(Category.from_dict, x), from_none], obj.get("category"))
        return Professional(rest_id, professional_type, category)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.rest_id is not None:
            result["rest_id"] = from_union([from_str, from_none], self.rest_id)
        if self.professional_type is not None:
            result["professional_type"] = from_union([from_str, from_none], self.professional_type)
        if self.category is not None:
            result["category"] = from_union([lambda x: from_list(lambda x: to_class(Category, x), x), from_none], self.category)
        return result


class ProfileImageShape(Enum):
    CIRCLE = "Circle"


class Typename(Enum):
    USER = "User"


@dataclass
class UserResultsResult:
    typename: Optional[Typename] = None
    id: Optional[ID] = None
    rest_id: Optional[str] = None
    affiliates_highlighted_label: Optional[UnmentionData] = None
    is_blue_verified: Optional[bool] = None
    profile_image_shape: Optional[ProfileImageShape] = None
    legacy: Optional[PurpleLegacy] = None
    professional: Optional[Professional] = None

    @staticmethod
    def from_dict(obj: Any) -> 'UserResultsResult':
        assert isinstance(obj, dict)
        typename = from_union([Typename, from_none], obj.get("__typename"))
        id = from_union([ID, from_none], obj.get("id"))
        rest_id = from_union([from_str, from_none], obj.get("rest_id"))
        affiliates_highlighted_label = from_union([UnmentionData.from_dict, from_none], obj.get("affiliates_highlighted_label"))
        is_blue_verified = from_union([from_bool, from_none], obj.get("is_blue_verified"))
        profile_image_shape = from_union([ProfileImageShape, from_none], obj.get("profile_image_shape"))
        legacy = from_union([PurpleLegacy.from_dict, from_none], obj.get("legacy"))
        professional = from_union([Professional.from_dict, from_none], obj.get("professional"))
        return UserResultsResult(typename, id, rest_id, affiliates_highlighted_label, is_blue_verified, profile_image_shape, legacy, professional)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.typename is not None:
            result["__typename"] = from_union([lambda x: to_enum(Typename, x), from_none], self.typename)
        if self.id is not None:
            result["id"] = from_union([lambda x: to_enum(ID, x), from_none], self.id)
        if self.rest_id is not None:
            result["rest_id"] = from_union([from_str, from_none], self.rest_id)
        if self.affiliates_highlighted_label is not None:
            result["affiliates_highlighted_label"] = from_union([lambda x: to_class(UnmentionData, x), from_none], self.affiliates_highlighted_label)
        if self.is_blue_verified is not None:
            result["is_blue_verified"] = from_union([from_bool, from_none], self.is_blue_verified)
        if self.profile_image_shape is not None:
            result["profile_image_shape"] = from_union([lambda x: to_enum(ProfileImageShape, x), from_none], self.profile_image_shape)
        if self.legacy is not None:
            result["legacy"] = from_union([lambda x: to_class(PurpleLegacy, x), from_none], self.legacy)
        if self.professional is not None:
            result["professional"] = from_union([lambda x: to_class(Professional, x), from_none], self.professional)
        return result


@dataclass
class UserRe:
    result: Optional[UserResultsResult] = None

    @staticmethod
    def from_dict(obj: Any) -> 'UserRe':
        assert isinstance(obj, dict)
        result = from_union([UserResultsResult.from_dict, from_none], obj.get("result"))
        return UserRe(result)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.result is not None:
            result["result"] = from_union([lambda x: to_class(UserResultsResult, x), from_none], self.result)
        return result


@dataclass
class CardLegacy:
    binding_values: Optional[List[BindingValue]] = None
    card_platform: Optional[CardPlatform] = None
    name: Optional[str] = None
    url: Optional[str] = None
    user_refs_results: Optional[List[UserRe]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'CardLegacy':
        assert isinstance(obj, dict)
        binding_values = from_union([lambda x: from_list(BindingValue.from_dict, x), from_none], obj.get("binding_values"))
        card_platform = from_union([CardPlatform.from_dict, from_none], obj.get("card_platform"))
        name = from_union([from_str, from_none], obj.get("name"))
        url = from_union([from_str, from_none], obj.get("url"))
        user_refs_results = from_union([lambda x: from_list(UserRe.from_dict, x), from_none], obj.get("user_refs_results"))
        return CardLegacy(binding_values, card_platform, name, url, user_refs_results)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.binding_values is not None:
            result["binding_values"] = from_union([lambda x: from_list(lambda x: to_class(BindingValue, x), x), from_none], self.binding_values)
        if self.card_platform is not None:
            result["card_platform"] = from_union([lambda x: to_class(CardPlatform, x), from_none], self.card_platform)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.url is not None:
            result["url"] = from_union([from_str, from_none], self.url)
        if self.user_refs_results is not None:
            result["user_refs_results"] = from_union([lambda x: from_list(lambda x: to_class(UserRe, x), x), from_none], self.user_refs_results)
        return result


@dataclass
class Card:
    rest_id: Optional[str] = None
    legacy: Optional[CardLegacy] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Card':
        assert isinstance(obj, dict)
        rest_id = from_union([from_str, from_none], obj.get("rest_id"))
        legacy = from_union([CardLegacy.from_dict, from_none], obj.get("legacy"))
        return Card(rest_id, legacy)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.rest_id is not None:
            result["rest_id"] = from_union([from_str, from_none], self.rest_id)
        if self.legacy is not None:
            result["legacy"] = from_union([lambda x: to_class(CardLegacy, x), from_none], self.legacy)
        return result


@dataclass
class Core:
    user_results: Optional[UserRe] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Core':
        assert isinstance(obj, dict)
        user_results = from_union([UserRe.from_dict, from_none], obj.get("user_results"))
        return Core(user_results)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.user_results is not None:
            result["user_results"] = from_union([lambda x: to_class(UserRe, x), from_none], self.user_results)
        return result


@dataclass
class EditControl:
    edits_remaining: Optional[int] = None
    edit_tweet_ids: Optional[List[str]] = None
    editable_until_msecs: Optional[str] = None
    is_edit_eligible: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'EditControl':
        assert isinstance(obj, dict)
        edits_remaining = from_union([from_none, lambda x: int(from_str(x))], obj.get("edits_remaining"))
        edit_tweet_ids = from_union([lambda x: from_list(from_str, x), from_none], obj.get("edit_tweet_ids"))
        editable_until_msecs = from_union([from_str, from_none], obj.get("editable_until_msecs"))
        is_edit_eligible = from_union([from_bool, from_none], obj.get("is_edit_eligible"))
        return EditControl(edits_remaining, edit_tweet_ids, editable_until_msecs, is_edit_eligible)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.edits_remaining is not None:
            result["edits_remaining"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.edits_remaining)
        if self.edit_tweet_ids is not None:
            result["edit_tweet_ids"] = from_union([lambda x: from_list(from_str, x), from_none], self.edit_tweet_ids)
        if self.editable_until_msecs is not None:
            result["editable_until_msecs"] = from_union([from_str, from_none], self.editable_until_msecs)
        if self.is_edit_eligible is not None:
            result["is_edit_eligible"] = from_union([from_bool, from_none], self.is_edit_eligible)
        return result


@dataclass
class Hashtag:
    indices: Optional[List[int]] = None
    text: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Hashtag':
        assert isinstance(obj, dict)
        indices = from_union([lambda x: from_list(from_int, x), from_none], obj.get("indices"))
        text = from_union([from_str, from_none], obj.get("text"))
        return Hashtag(indices, text)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.indices is not None:
            result["indices"] = from_union([lambda x: from_list(from_int, x), from_none], self.indices)
        if self.text is not None:
            result["text"] = from_union([from_str, from_none], self.text)
        return result


class Status(Enum):
    AVAILABLE = "Available"


@dataclass
class EXTMediaAvailability:
    status: Optional[Status] = None

    @staticmethod
    def from_dict(obj: Any) -> 'EXTMediaAvailability':
        assert isinstance(obj, dict)
        status = from_union([Status, from_none], obj.get("status"))
        return EXTMediaAvailability(status)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.status is not None:
            result["status"] = from_union([lambda x: to_enum(Status, x), from_none], self.status)
        return result


@dataclass
class FocusRect:
    x: Optional[int] = None
    y: Optional[int] = None
    h: Optional[int] = None
    w: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'FocusRect':
        assert isinstance(obj, dict)
        x = from_union([from_int, from_none], obj.get("x"))
        y = from_union([from_int, from_none], obj.get("y"))
        h = from_union([from_int, from_none], obj.get("h"))
        w = from_union([from_int, from_none], obj.get("w"))
        return FocusRect(x, y, h, w)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.x is not None:
            result["x"] = from_union([from_int, from_none], self.x)
        if self.y is not None:
            result["y"] = from_union([from_int, from_none], self.y)
        if self.h is not None:
            result["h"] = from_union([from_int, from_none], self.h)
        if self.w is not None:
            result["w"] = from_union([from_int, from_none], self.w)
        return result


@dataclass
class OrigClass:
    faces: Optional[List[FocusRect]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'OrigClass':
        assert isinstance(obj, dict)
        faces = from_union([lambda x: from_list(FocusRect.from_dict, x), from_none], obj.get("faces"))
        return OrigClass(faces)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.faces is not None:
            result["faces"] = from_union([lambda x: from_list(lambda x: to_class(FocusRect, x), x), from_none], self.faces)
        return result


@dataclass
class Features:
    large: Optional[OrigClass] = None
    medium: Optional[OrigClass] = None
    small: Optional[OrigClass] = None
    orig: Optional[OrigClass] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Features':
        assert isinstance(obj, dict)
        large = from_union([OrigClass.from_dict, from_none], obj.get("large"))
        medium = from_union([OrigClass.from_dict, from_none], obj.get("medium"))
        small = from_union([OrigClass.from_dict, from_none], obj.get("small"))
        orig = from_union([OrigClass.from_dict, from_none], obj.get("orig"))
        return Features(large, medium, small, orig)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.large is not None:
            result["large"] = from_union([lambda x: to_class(OrigClass, x), from_none], self.large)
        if self.medium is not None:
            result["medium"] = from_union([lambda x: to_class(OrigClass, x), from_none], self.medium)
        if self.small is not None:
            result["small"] = from_union([lambda x: to_class(OrigClass, x), from_none], self.small)
        if self.orig is not None:
            result["orig"] = from_union([lambda x: to_class(OrigClass, x), from_none], self.orig)
        return result


@dataclass
class OriginalInfo:
    height: Optional[int] = None
    width: Optional[int] = None
    focus_rects: Optional[List[FocusRect]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'OriginalInfo':
        assert isinstance(obj, dict)
        height = from_union([from_int, from_none], obj.get("height"))
        width = from_union([from_int, from_none], obj.get("width"))
        focus_rects = from_union([lambda x: from_list(FocusRect.from_dict, x), from_none], obj.get("focus_rects"))
        return OriginalInfo(height, width, focus_rects)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.height is not None:
            result["height"] = from_union([from_int, from_none], self.height)
        if self.width is not None:
            result["width"] = from_union([from_int, from_none], self.width)
        if self.focus_rects is not None:
            result["focus_rects"] = from_union([lambda x: from_list(lambda x: to_class(FocusRect, x), x), from_none], self.focus_rects)
        return result


class Resize(Enum):
    CROP = "crop"
    FIT = "fit"


@dataclass
class ThumbClass:
    h: Optional[int] = None
    w: Optional[int] = None
    resize: Optional[Resize] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ThumbClass':
        assert isinstance(obj, dict)
        h = from_union([from_int, from_none], obj.get("h"))
        w = from_union([from_int, from_none], obj.get("w"))
        resize = from_union([Resize, from_none], obj.get("resize"))
        return ThumbClass(h, w, resize)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.h is not None:
            result["h"] = from_union([from_int, from_none], self.h)
        if self.w is not None:
            result["w"] = from_union([from_int, from_none], self.w)
        if self.resize is not None:
            result["resize"] = from_union([lambda x: to_enum(Resize, x), from_none], self.resize)
        return result


@dataclass
class Sizes:
    large: Optional[ThumbClass] = None
    medium: Optional[ThumbClass] = None
    small: Optional[ThumbClass] = None
    thumb: Optional[ThumbClass] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Sizes':
        assert isinstance(obj, dict)
        large = from_union([ThumbClass.from_dict, from_none], obj.get("large"))
        medium = from_union([ThumbClass.from_dict, from_none], obj.get("medium"))
        small = from_union([ThumbClass.from_dict, from_none], obj.get("small"))
        thumb = from_union([ThumbClass.from_dict, from_none], obj.get("thumb"))
        return Sizes(large, medium, small, thumb)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.large is not None:
            result["large"] = from_union([lambda x: to_class(ThumbClass, x), from_none], self.large)
        if self.medium is not None:
            result["medium"] = from_union([lambda x: to_class(ThumbClass, x), from_none], self.medium)
        if self.small is not None:
            result["small"] = from_union([lambda x: to_class(ThumbClass, x), from_none], self.small)
        if self.thumb is not None:
            result["thumb"] = from_union([lambda x: to_class(ThumbClass, x), from_none], self.thumb)
        return result


class MediaType(Enum):
    ANIMATED_GIF = "animated_gif"
    PHOTO = "photo"
    VIDEO = "video"


@dataclass
class EntitiesMedia:
    display_url: Optional[str] = None
    expanded_url: Optional[str] = None
    id_str: Optional[str] = None
    indices: Optional[List[int]] = None
    media_url_https: Optional[str] = None
    type: Optional[MediaType] = None
    url: Optional[str] = None
    features: Optional[Features] = None
    sizes: Optional[Sizes] = None
    original_info: Optional[OriginalInfo] = None
    media_key: Optional[str] = None
    ext_media_availability: Optional[EXTMediaAvailability] = None

    @staticmethod
    def from_dict(obj: Any) -> 'EntitiesMedia':
        assert isinstance(obj, dict)
        display_url = from_union([from_str, from_none], obj.get("display_url"))
        expanded_url = from_union([from_str, from_none], obj.get("expanded_url"))
        id_str = from_union([from_str, from_none], obj.get("id_str"))
        indices = from_union([lambda x: from_list(from_int, x), from_none], obj.get("indices"))
        media_url_https = from_union([from_str, from_none], obj.get("media_url_https"))
        type = from_union([MediaType, from_none], obj.get("type"))
        url = from_union([from_str, from_none], obj.get("url"))
        features = from_union([Features.from_dict, from_none], obj.get("features"))
        sizes = from_union([Sizes.from_dict, from_none], obj.get("sizes"))
        original_info = from_union([OriginalInfo.from_dict, from_none], obj.get("original_info"))
        media_key = from_union([from_str, from_none], obj.get("media_key"))
        ext_media_availability = from_union([EXTMediaAvailability.from_dict, from_none], obj.get("ext_media_availability"))
        return EntitiesMedia(display_url, expanded_url, id_str, indices, media_url_https, type, url, features, sizes, original_info, media_key, ext_media_availability)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.display_url is not None:
            result["display_url"] = from_union([from_str, from_none], self.display_url)
        if self.expanded_url is not None:
            result["expanded_url"] = from_union([from_str, from_none], self.expanded_url)
        if self.id_str is not None:
            result["id_str"] = from_union([from_str, from_none], self.id_str)
        if self.indices is not None:
            result["indices"] = from_union([lambda x: from_list(from_int, x), from_none], self.indices)
        if self.media_url_https is not None:
            result["media_url_https"] = from_union([from_str, from_none], self.media_url_https)
        if self.type is not None:
            result["type"] = from_union([lambda x: to_enum(MediaType, x), from_none], self.type)
        if self.url is not None:
            result["url"] = from_union([from_str, from_none], self.url)
        if self.features is not None:
            result["features"] = from_union([lambda x: to_class(Features, x), from_none], self.features)
        if self.sizes is not None:
            result["sizes"] = from_union([lambda x: to_class(Sizes, x), from_none], self.sizes)
        if self.original_info is not None:
            result["original_info"] = from_union([lambda x: to_class(OriginalInfo, x), from_none], self.original_info)
        if self.media_key is not None:
            result["media_key"] = from_union([from_str, from_none], self.media_key)
        if self.ext_media_availability is not None:
            result["ext_media_availability"] = from_union([lambda x: to_class(EXTMediaAvailability, x), from_none], self.ext_media_availability)
        return result


@dataclass
class UserMention:
    id_str: Optional[str] = None
    name: Optional[str] = None
    screen_name: Optional[str] = None
    indices: Optional[List[int]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'UserMention':
        assert isinstance(obj, dict)
        id_str = from_union([from_str, from_none], obj.get("id_str"))
        name = from_union([from_str, from_none], obj.get("name"))
        screen_name = from_union([from_str, from_none], obj.get("screen_name"))
        indices = from_union([lambda x: from_list(from_int, x), from_none], obj.get("indices"))
        return UserMention(id_str, name, screen_name, indices)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.id_str is not None:
            result["id_str"] = from_union([from_str, from_none], self.id_str)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.screen_name is not None:
            result["screen_name"] = from_union([from_str, from_none], self.screen_name)
        if self.indices is not None:
            result["indices"] = from_union([lambda x: from_list(from_int, x), from_none], self.indices)
        return result


@dataclass
class FluffyEntities:
    user_mentions: Optional[List[UserMention]] = None
    urls: Optional[List[URL]] = None
    hashtags: Optional[List[Hashtag]] = None
    symbols: Optional[List[Any]] = None
    media: Optional[List[EntitiesMedia]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'FluffyEntities':
        assert isinstance(obj, dict)
        user_mentions = from_union([lambda x: from_list(UserMention.from_dict, x), from_none], obj.get("user_mentions"))
        urls = from_union([lambda x: from_list(URL.from_dict, x), from_none], obj.get("urls"))
        hashtags = from_union([lambda x: from_list(Hashtag.from_dict, x), from_none], obj.get("hashtags"))
        symbols = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("symbols"))
        media = from_union([lambda x: from_list(EntitiesMedia.from_dict, x), from_none], obj.get("media"))
        return FluffyEntities(user_mentions, urls, hashtags, symbols, media)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.user_mentions is not None:
            result["user_mentions"] = from_union([lambda x: from_list(lambda x: to_class(UserMention, x), x), from_none], self.user_mentions)
        if self.urls is not None:
            result["urls"] = from_union([lambda x: from_list(lambda x: to_class(URL, x), x), from_none], self.urls)
        if self.hashtags is not None:
            result["hashtags"] = from_union([lambda x: from_list(lambda x: to_class(Hashtag, x), x), from_none], self.hashtags)
        if self.symbols is not None:
            result["symbols"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.symbols)
        if self.media is not None:
            result["media"] = from_union([lambda x: from_list(lambda x: to_class(EntitiesMedia, x), x), from_none], self.media)
        return result


@dataclass
class AdditionalMediaInfo:
    monetizable: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AdditionalMediaInfo':
        assert isinstance(obj, dict)
        monetizable = from_union([from_bool, from_none], obj.get("monetizable"))
        return AdditionalMediaInfo(monetizable)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.monetizable is not None:
            result["monetizable"] = from_union([from_bool, from_none], self.monetizable)
        return result


@dataclass
class MediaStats:
    view_count: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'MediaStats':
        assert isinstance(obj, dict)
        view_count = from_union([from_int, from_none], obj.get("viewCount"))
        return MediaStats(view_count)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.view_count is not None:
            result["viewCount"] = from_union([from_int, from_none], self.view_count)
        return result


class ContentType(Enum):
    APPLICATION_X_MPEG_URL = "application/x-mpegURL"
    VIDEO_MP4 = "video/mp4"


@dataclass
class Variant:
    bitrate: Optional[int] = None
    content_type: Optional[ContentType] = None
    url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Variant':
        assert isinstance(obj, dict)
        bitrate = from_union([from_int, from_none], obj.get("bitrate"))
        content_type = from_union([ContentType, from_none], obj.get("content_type"))
        url = from_union([from_str, from_none], obj.get("url"))
        return Variant(bitrate, content_type, url)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.bitrate is not None:
            result["bitrate"] = from_union([from_int, from_none], self.bitrate)
        if self.content_type is not None:
            result["content_type"] = from_union([lambda x: to_enum(ContentType, x), from_none], self.content_type)
        if self.url is not None:
            result["url"] = from_union([from_str, from_none], self.url)
        return result


@dataclass
class VideoInfo:
    aspect_ratio: Optional[List[int]] = None
    duration_millis: Optional[int] = None
    variants: Optional[List[Variant]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'VideoInfo':
        assert isinstance(obj, dict)
        aspect_ratio = from_union([lambda x: from_list(from_int, x), from_none], obj.get("aspect_ratio"))
        duration_millis = from_union([from_int, from_none], obj.get("duration_millis"))
        variants = from_union([lambda x: from_list(Variant.from_dict, x), from_none], obj.get("variants"))
        return VideoInfo(aspect_ratio, duration_millis, variants)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.aspect_ratio is not None:
            result["aspect_ratio"] = from_union([lambda x: from_list(from_int, x), from_none], self.aspect_ratio)
        if self.duration_millis is not None:
            result["duration_millis"] = from_union([from_int, from_none], self.duration_millis)
        if self.variants is not None:
            result["variants"] = from_union([lambda x: from_list(lambda x: to_class(Variant, x), x), from_none], self.variants)
        return result


@dataclass
class PurpleMedia:
    display_url: Optional[str] = None
    expanded_url: Optional[str] = None
    id_str: Optional[str] = None
    indices: Optional[List[int]] = None
    media_key: Optional[str] = None
    media_url_https: Optional[str] = None
    type: Optional[MediaType] = None
    url: Optional[str] = None
    ext_media_availability: Optional[EXTMediaAvailability] = None
    features: Optional[Features] = None
    sizes: Optional[Sizes] = None
    original_info: Optional[OriginalInfo] = None
    ext_alt_text: Optional[str] = None
    additional_media_info: Optional[AdditionalMediaInfo] = None
    media_stats: Optional[MediaStats] = None
    video_info: Optional[VideoInfo] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PurpleMedia':
        assert isinstance(obj, dict)
        display_url = from_union([from_str, from_none], obj.get("display_url"))
        expanded_url = from_union([from_str, from_none], obj.get("expanded_url"))
        id_str = from_union([from_str, from_none], obj.get("id_str"))
        indices = from_union([lambda x: from_list(from_int, x), from_none], obj.get("indices"))
        media_key = from_union([from_str, from_none], obj.get("media_key"))
        media_url_https = from_union([from_str, from_none], obj.get("media_url_https"))
        type = from_union([MediaType, from_none], obj.get("type"))
        url = from_union([from_str, from_none], obj.get("url"))
        ext_media_availability = from_union([EXTMediaAvailability.from_dict, from_none], obj.get("ext_media_availability"))
        features = from_union([Features.from_dict, from_none], obj.get("features"))
        sizes = from_union([Sizes.from_dict, from_none], obj.get("sizes"))
        original_info = from_union([OriginalInfo.from_dict, from_none], obj.get("original_info"))
        ext_alt_text = from_union([from_str, from_none], obj.get("ext_alt_text"))
        additional_media_info = from_union([AdditionalMediaInfo.from_dict, from_none], obj.get("additional_media_info"))
        media_stats = from_union([MediaStats.from_dict, from_none], obj.get("mediaStats"))
        video_info = from_union([VideoInfo.from_dict, from_none], obj.get("video_info"))
        return PurpleMedia(display_url, expanded_url, id_str, indices, media_key, media_url_https, type, url, ext_media_availability, features, sizes, original_info, ext_alt_text, additional_media_info, media_stats, video_info)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.display_url is not None:
            result["display_url"] = from_union([from_str, from_none], self.display_url)
        if self.expanded_url is not None:
            result["expanded_url"] = from_union([from_str, from_none], self.expanded_url)
        if self.id_str is not None:
            result["id_str"] = from_union([from_str, from_none], self.id_str)
        if self.indices is not None:
            result["indices"] = from_union([lambda x: from_list(from_int, x), from_none], self.indices)
        if self.media_key is not None:
            result["media_key"] = from_union([from_str, from_none], self.media_key)
        if self.media_url_https is not None:
            result["media_url_https"] = from_union([from_str, from_none], self.media_url_https)
        if self.type is not None:
            result["type"] = from_union([lambda x: to_enum(MediaType, x), from_none], self.type)
        if self.url is not None:
            result["url"] = from_union([from_str, from_none], self.url)
        if self.ext_media_availability is not None:
            result["ext_media_availability"] = from_union([lambda x: to_class(EXTMediaAvailability, x), from_none], self.ext_media_availability)
        if self.features is not None:
            result["features"] = from_union([lambda x: to_class(Features, x), from_none], self.features)
        if self.sizes is not None:
            result["sizes"] = from_union([lambda x: to_class(Sizes, x), from_none], self.sizes)
        if self.original_info is not None:
            result["original_info"] = from_union([lambda x: to_class(OriginalInfo, x), from_none], self.original_info)
        if self.ext_alt_text is not None:
            result["ext_alt_text"] = from_union([from_str, from_none], self.ext_alt_text)
        if self.additional_media_info is not None:
            result["additional_media_info"] = from_union([lambda x: to_class(AdditionalMediaInfo, x), from_none], self.additional_media_info)
        if self.media_stats is not None:
            result["mediaStats"] = from_union([lambda x: to_class(MediaStats, x), from_none], self.media_stats)
        if self.video_info is not None:
            result["video_info"] = from_union([lambda x: to_class(VideoInfo, x), from_none], self.video_info)
        return result


@dataclass
class PurpleExtendedEntities:
    media: Optional[List[PurpleMedia]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PurpleExtendedEntities':
        assert isinstance(obj, dict)
        media = from_union([lambda x: from_list(PurpleMedia.from_dict, x), from_none], obj.get("media"))
        return PurpleExtendedEntities(media)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.media is not None:
            result["media"] = from_union([lambda x: from_list(lambda x: to_class(PurpleMedia, x), x), from_none], self.media)
        return result


class Lang(Enum):
    DA = "da"
    DE = "de"
    FI = "fi"
    NO = "no"
    SV = "sv"
    ZXX = "zxx"


@dataclass
class QuotedStatusPermalink:
    url: Optional[str] = None
    expanded: Optional[str] = None
    display: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'QuotedStatusPermalink':
        assert isinstance(obj, dict)
        url = from_union([from_str, from_none], obj.get("url"))
        expanded = from_union([from_str, from_none], obj.get("expanded"))
        display = from_union([from_str, from_none], obj.get("display"))
        return QuotedStatusPermalink(url, expanded, display)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.url is not None:
            result["url"] = from_union([from_str, from_none], self.url)
        if self.expanded is not None:
            result["expanded"] = from_union([from_str, from_none], self.expanded)
        if self.display is not None:
            result["display"] = from_union([from_str, from_none], self.display)
        return result


@dataclass
class FluffyExtendedEntities:
    media: Optional[List[EntitiesMedia]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'FluffyExtendedEntities':
        assert isinstance(obj, dict)
        media = from_union([lambda x: from_list(EntitiesMedia.from_dict, x), from_none], obj.get("media"))
        return FluffyExtendedEntities(media)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.media is not None:
            result["media"] = from_union([lambda x: from_list(lambda x: to_class(EntitiesMedia, x), x), from_none], self.media)
        return result


@dataclass
class SelfThread:
    id_str: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SelfThread':
        assert isinstance(obj, dict)
        id_str = from_union([from_str, from_none], obj.get("id_str"))
        return SelfThread(id_str)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.id_str is not None:
            result["id_str"] = from_union([from_str, from_none], self.id_str)
        return result


@dataclass
class TentacledLegacy:
    bookmark_count: Optional[int] = None
    bookmarked: Optional[bool] = None
    created_at: Optional[str] = None
    conversation_id_str: Optional[str] = None
    display_text_range: Optional[List[int]] = None
    entities: Optional[FluffyEntities] = None
    favorite_count: Optional[int] = None
    favorited: Optional[bool] = None
    full_text: Optional[str] = None
    is_quote_status: Optional[bool] = None
    lang: Optional[Lang] = None
    quote_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None
    retweeted: Optional[bool] = None
    user_id_str: Optional[str] = None
    id_str: Optional[str] = None
    self_thread: Optional[SelfThread] = None
    quoted_status_id_str: Optional[str] = None
    quoted_status_permalink: Optional[QuotedStatusPermalink] = None
    extended_entities: Optional[FluffyExtendedEntities] = None
    possibly_sensitive: Optional[bool] = None
    possibly_sensitive_editable: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TentacledLegacy':
        assert isinstance(obj, dict)
        bookmark_count = from_union([from_int, from_none], obj.get("bookmark_count"))
        bookmarked = from_union([from_bool, from_none], obj.get("bookmarked"))
        created_at = from_union([from_str, from_none], obj.get("created_at"))
        conversation_id_str = from_union([from_str, from_none], obj.get("conversation_id_str"))
        display_text_range = from_union([lambda x: from_list(from_int, x), from_none], obj.get("display_text_range"))
        entities = from_union([FluffyEntities.from_dict, from_none], obj.get("entities"))
        favorite_count = from_union([from_int, from_none], obj.get("favorite_count"))
        favorited = from_union([from_bool, from_none], obj.get("favorited"))
        full_text = from_union([from_str, from_none], obj.get("full_text"))
        is_quote_status = from_union([from_bool, from_none], obj.get("is_quote_status"))
        lang = from_union([Lang, from_none], obj.get("lang"))
        quote_count = from_union([from_int, from_none], obj.get("quote_count"))
        reply_count = from_union([from_int, from_none], obj.get("reply_count"))
        retweet_count = from_union([from_int, from_none], obj.get("retweet_count"))
        retweeted = from_union([from_bool, from_none], obj.get("retweeted"))
        user_id_str = from_union([from_str, from_none], obj.get("user_id_str"))
        id_str = from_union([from_str, from_none], obj.get("id_str"))
        self_thread = from_union([SelfThread.from_dict, from_none], obj.get("self_thread"))
        quoted_status_id_str = from_union([from_str, from_none], obj.get("quoted_status_id_str"))
        quoted_status_permalink = from_union([QuotedStatusPermalink.from_dict, from_none], obj.get("quoted_status_permalink"))
        extended_entities = from_union([FluffyExtendedEntities.from_dict, from_none], obj.get("extended_entities"))
        possibly_sensitive = from_union([from_bool, from_none], obj.get("possibly_sensitive"))
        possibly_sensitive_editable = from_union([from_bool, from_none], obj.get("possibly_sensitive_editable"))
        return TentacledLegacy(bookmark_count, bookmarked, created_at, conversation_id_str, display_text_range, entities, favorite_count, favorited, full_text, is_quote_status, lang, quote_count, reply_count, retweet_count, retweeted, user_id_str, id_str, self_thread, quoted_status_id_str, quoted_status_permalink, extended_entities, possibly_sensitive, possibly_sensitive_editable)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.bookmark_count is not None:
            result["bookmark_count"] = from_union([from_int, from_none], self.bookmark_count)
        if self.bookmarked is not None:
            result["bookmarked"] = from_union([from_bool, from_none], self.bookmarked)
        if self.created_at is not None:
            result["created_at"] = from_union([from_str, from_none], self.created_at)
        if self.conversation_id_str is not None:
            result["conversation_id_str"] = from_union([from_str, from_none], self.conversation_id_str)
        if self.display_text_range is not None:
            result["display_text_range"] = from_union([lambda x: from_list(from_int, x), from_none], self.display_text_range)
        if self.entities is not None:
            result["entities"] = from_union([lambda x: to_class(FluffyEntities, x), from_none], self.entities)
        if self.favorite_count is not None:
            result["favorite_count"] = from_union([from_int, from_none], self.favorite_count)
        if self.favorited is not None:
            result["favorited"] = from_union([from_bool, from_none], self.favorited)
        if self.full_text is not None:
            result["full_text"] = from_union([from_str, from_none], self.full_text)
        if self.is_quote_status is not None:
            result["is_quote_status"] = from_union([from_bool, from_none], self.is_quote_status)
        if self.lang is not None:
            result["lang"] = from_union([lambda x: to_enum(Lang, x), from_none], self.lang)
        if self.quote_count is not None:
            result["quote_count"] = from_union([from_int, from_none], self.quote_count)
        if self.reply_count is not None:
            result["reply_count"] = from_union([from_int, from_none], self.reply_count)
        if self.retweet_count is not None:
            result["retweet_count"] = from_union([from_int, from_none], self.retweet_count)
        if self.retweeted is not None:
            result["retweeted"] = from_union([from_bool, from_none], self.retweeted)
        if self.user_id_str is not None:
            result["user_id_str"] = from_union([from_str, from_none], self.user_id_str)
        if self.id_str is not None:
            result["id_str"] = from_union([from_str, from_none], self.id_str)
        if self.self_thread is not None:
            result["self_thread"] = from_union([lambda x: to_class(SelfThread, x), from_none], self.self_thread)
        if self.quoted_status_id_str is not None:
            result["quoted_status_id_str"] = from_union([from_str, from_none], self.quoted_status_id_str)
        if self.quoted_status_permalink is not None:
            result["quoted_status_permalink"] = from_union([lambda x: to_class(QuotedStatusPermalink, x), from_none], self.quoted_status_permalink)
        if self.extended_entities is not None:
            result["extended_entities"] = from_union([lambda x: to_class(FluffyExtendedEntities, x), from_none], self.extended_entities)
        if self.possibly_sensitive is not None:
            result["possibly_sensitive"] = from_union([from_bool, from_none], self.possibly_sensitive)
        if self.possibly_sensitive_editable is not None:
            result["possibly_sensitive_editable"] = from_union([from_bool, from_none], self.possibly_sensitive_editable)
        return result


@dataclass
class StickyLegacy:
    bookmark_count: Optional[int] = None
    bookmarked: Optional[bool] = None
    created_at: Optional[str] = None
    conversation_id_str: Optional[str] = None
    display_text_range: Optional[List[int]] = None
    entities: Optional[FluffyEntities] = None
    favorite_count: Optional[int] = None
    favorited: Optional[bool] = None
    full_text: Optional[str] = None
    is_quote_status: Optional[bool] = None
    lang: Optional[Lang] = None
    quote_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None
    retweeted: Optional[bool] = None
    user_id_str: Optional[str] = None
    id_str: Optional[str] = None
    self_thread: Optional[SelfThread] = None

    @staticmethod
    def from_dict(obj: Any) -> 'StickyLegacy':
        assert isinstance(obj, dict)
        bookmark_count = from_union([from_int, from_none], obj.get("bookmark_count"))
        bookmarked = from_union([from_bool, from_none], obj.get("bookmarked"))
        created_at = from_union([from_str, from_none], obj.get("created_at"))
        conversation_id_str = from_union([from_str, from_none], obj.get("conversation_id_str"))
        display_text_range = from_union([lambda x: from_list(from_int, x), from_none], obj.get("display_text_range"))
        entities = from_union([FluffyEntities.from_dict, from_none], obj.get("entities"))
        favorite_count = from_union([from_int, from_none], obj.get("favorite_count"))
        favorited = from_union([from_bool, from_none], obj.get("favorited"))
        full_text = from_union([from_str, from_none], obj.get("full_text"))
        is_quote_status = from_union([from_bool, from_none], obj.get("is_quote_status"))
        lang = from_union([Lang, from_none], obj.get("lang"))
        quote_count = from_union([from_int, from_none], obj.get("quote_count"))
        reply_count = from_union([from_int, from_none], obj.get("reply_count"))
        retweet_count = from_union([from_int, from_none], obj.get("retweet_count"))
        retweeted = from_union([from_bool, from_none], obj.get("retweeted"))
        user_id_str = from_union([from_str, from_none], obj.get("user_id_str"))
        id_str = from_union([from_str, from_none], obj.get("id_str"))
        self_thread = from_union([SelfThread.from_dict, from_none], obj.get("self_thread"))
        return StickyLegacy(bookmark_count, bookmarked, created_at, conversation_id_str, display_text_range, entities, favorite_count, favorited, full_text, is_quote_status, lang, quote_count, reply_count, retweet_count, retweeted, user_id_str, id_str, self_thread)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.bookmark_count is not None:
            result["bookmark_count"] = from_union([from_int, from_none], self.bookmark_count)
        if self.bookmarked is not None:
            result["bookmarked"] = from_union([from_bool, from_none], self.bookmarked)
        if self.created_at is not None:
            result["created_at"] = from_union([from_str, from_none], self.created_at)
        if self.conversation_id_str is not None:
            result["conversation_id_str"] = from_union([from_str, from_none], self.conversation_id_str)
        if self.display_text_range is not None:
            result["display_text_range"] = from_union([lambda x: from_list(from_int, x), from_none], self.display_text_range)
        if self.entities is not None:
            result["entities"] = from_union([lambda x: to_class(FluffyEntities, x), from_none], self.entities)
        if self.favorite_count is not None:
            result["favorite_count"] = from_union([from_int, from_none], self.favorite_count)
        if self.favorited is not None:
            result["favorited"] = from_union([from_bool, from_none], self.favorited)
        if self.full_text is not None:
            result["full_text"] = from_union([from_str, from_none], self.full_text)
        if self.is_quote_status is not None:
            result["is_quote_status"] = from_union([from_bool, from_none], self.is_quote_status)
        if self.lang is not None:
            result["lang"] = from_union([lambda x: to_enum(Lang, x), from_none], self.lang)
        if self.quote_count is not None:
            result["quote_count"] = from_union([from_int, from_none], self.quote_count)
        if self.reply_count is not None:
            result["reply_count"] = from_union([from_int, from_none], self.reply_count)
        if self.retweet_count is not None:
            result["retweet_count"] = from_union([from_int, from_none], self.retweet_count)
        if self.retweeted is not None:
            result["retweeted"] = from_union([from_bool, from_none], self.retweeted)
        if self.user_id_str is not None:
            result["user_id_str"] = from_union([from_str, from_none], self.user_id_str)
        if self.id_str is not None:
            result["id_str"] = from_union([from_str, from_none], self.id_str)
        if self.self_thread is not None:
            result["self_thread"] = from_union([lambda x: to_class(SelfThread, x), from_none], self.self_thread)
        return result


class State(Enum):
    ENABLED = "Enabled"
    ENABLED_WITH_COUNT = "EnabledWithCount"


@dataclass
class Views:
    count: Optional[int] = None
    state: Optional[State] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Views':
        assert isinstance(obj, dict)
        count = from_union([from_none, lambda x: int(from_str(x))], obj.get("count"))
        state = from_union([State, from_none], obj.get("state"))
        return Views(count, state)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.count is not None:
            result["count"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.count)
        if self.state is not None:
            result["state"] = from_union([lambda x: to_enum(State, x), from_none], self.state)
        return result


@dataclass
class QuotedStatusResultResult:
    typename: Optional[TweetDisplayType] = None
    rest_id: Optional[str] = None
    has_birdwatch_notes: Optional[bool] = None
    core: Optional[Core] = None
    unmention_data: Optional[UnmentionData] = None
    edit_control: Optional[EditControl] = None
    is_translatable: Optional[bool] = None
    views: Optional[Views] = None
    source: Optional[str] = None
    legacy: Optional[StickyLegacy] = None

    @staticmethod
    def from_dict(obj: Any) -> 'QuotedStatusResultResult':
        assert isinstance(obj, dict)
        typename = from_union([TweetDisplayType, from_none], obj.get("__typename"))
        rest_id = from_union([from_str, from_none], obj.get("rest_id"))
        has_birdwatch_notes = from_union([from_bool, from_none], obj.get("has_birdwatch_notes"))
        core = from_union([Core.from_dict, from_none], obj.get("core"))
        unmention_data = from_union([UnmentionData.from_dict, from_none], obj.get("unmention_data"))
        edit_control = from_union([EditControl.from_dict, from_none], obj.get("edit_control"))
        is_translatable = from_union([from_bool, from_none], obj.get("is_translatable"))
        views = from_union([Views.from_dict, from_none], obj.get("views"))
        source = from_union([from_str, from_none], obj.get("source"))
        legacy = from_union([StickyLegacy.from_dict, from_none], obj.get("legacy"))
        return QuotedStatusResultResult(typename, rest_id, has_birdwatch_notes, core, unmention_data, edit_control, is_translatable, views, source, legacy)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.typename is not None:
            result["__typename"] = from_union([lambda x: to_enum(TweetDisplayType, x), from_none], self.typename)
        if self.rest_id is not None:
            result["rest_id"] = from_union([from_str, from_none], self.rest_id)
        if self.has_birdwatch_notes is not None:
            result["has_birdwatch_notes"] = from_union([from_bool, from_none], self.has_birdwatch_notes)
        if self.core is not None:
            result["core"] = from_union([lambda x: to_class(Core, x), from_none], self.core)
        if self.unmention_data is not None:
            result["unmention_data"] = from_union([lambda x: to_class(UnmentionData, x), from_none], self.unmention_data)
        if self.edit_control is not None:
            result["edit_control"] = from_union([lambda x: to_class(EditControl, x), from_none], self.edit_control)
        if self.is_translatable is not None:
            result["is_translatable"] = from_union([from_bool, from_none], self.is_translatable)
        if self.views is not None:
            result["views"] = from_union([lambda x: to_class(Views, x), from_none], self.views)
        if self.source is not None:
            result["source"] = from_union([from_str, from_none], self.source)
        if self.legacy is not None:
            result["legacy"] = from_union([lambda x: to_class(StickyLegacy, x), from_none], self.legacy)
        return result


@dataclass
class QuotedStatusResult:
    result: Optional[QuotedStatusResultResult] = None

    @staticmethod
    def from_dict(obj: Any) -> 'QuotedStatusResult':
        assert isinstance(obj, dict)
        result = from_union([QuotedStatusResultResult.from_dict, from_none], obj.get("result"))
        return QuotedStatusResult(result)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.result is not None:
            result["result"] = from_union([lambda x: to_class(QuotedStatusResultResult, x), from_none], self.result)
        return result


@dataclass
class RetweetedStatusResultResult:
    typename: Optional[TweetDisplayType] = None
    rest_id: Optional[str] = None
    has_birdwatch_notes: Optional[bool] = None
    core: Optional[Core] = None
    unmention_data: Optional[UnmentionData] = None
    edit_control: Optional[EditControl] = None
    is_translatable: Optional[bool] = None
    views: Optional[Views] = None
    source: Optional[str] = None
    legacy: Optional[TentacledLegacy] = None
    quoted_status_result: Optional[QuotedStatusResult] = None

    @staticmethod
    def from_dict(obj: Any) -> 'RetweetedStatusResultResult':
        assert isinstance(obj, dict)
        typename = from_union([TweetDisplayType, from_none], obj.get("__typename"))
        rest_id = from_union([from_str, from_none], obj.get("rest_id"))
        has_birdwatch_notes = from_union([from_bool, from_none], obj.get("has_birdwatch_notes"))
        core = from_union([Core.from_dict, from_none], obj.get("core"))
        unmention_data = from_union([UnmentionData.from_dict, from_none], obj.get("unmention_data"))
        edit_control = from_union([EditControl.from_dict, from_none], obj.get("edit_control"))
        is_translatable = from_union([from_bool, from_none], obj.get("is_translatable"))
        views = from_union([Views.from_dict, from_none], obj.get("views"))
        source = from_union([from_str, from_none], obj.get("source"))
        legacy = from_union([TentacledLegacy.from_dict, from_none], obj.get("legacy"))
        quoted_status_result = from_union([QuotedStatusResult.from_dict, from_none], obj.get("quoted_status_result"))
        return RetweetedStatusResultResult(typename, rest_id, has_birdwatch_notes, core, unmention_data, edit_control, is_translatable, views, source, legacy, quoted_status_result)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.typename is not None:
            result["__typename"] = from_union([lambda x: to_enum(TweetDisplayType, x), from_none], self.typename)
        if self.rest_id is not None:
            result["rest_id"] = from_union([from_str, from_none], self.rest_id)
        if self.has_birdwatch_notes is not None:
            result["has_birdwatch_notes"] = from_union([from_bool, from_none], self.has_birdwatch_notes)
        if self.core is not None:
            result["core"] = from_union([lambda x: to_class(Core, x), from_none], self.core)
        if self.unmention_data is not None:
            result["unmention_data"] = from_union([lambda x: to_class(UnmentionData, x), from_none], self.unmention_data)
        if self.edit_control is not None:
            result["edit_control"] = from_union([lambda x: to_class(EditControl, x), from_none], self.edit_control)
        if self.is_translatable is not None:
            result["is_translatable"] = from_union([from_bool, from_none], self.is_translatable)
        if self.views is not None:
            result["views"] = from_union([lambda x: to_class(Views, x), from_none], self.views)
        if self.source is not None:
            result["source"] = from_union([from_str, from_none], self.source)
        if self.legacy is not None:
            result["legacy"] = from_union([lambda x: to_class(TentacledLegacy, x), from_none], self.legacy)
        if self.quoted_status_result is not None:
            result["quoted_status_result"] = from_union([lambda x: to_class(QuotedStatusResult, x), from_none], self.quoted_status_result)
        return result


@dataclass
class RetweetedStatusResult:
    result: Optional[RetweetedStatusResultResult] = None

    @staticmethod
    def from_dict(obj: Any) -> 'RetweetedStatusResult':
        assert isinstance(obj, dict)
        result = from_union([RetweetedStatusResultResult.from_dict, from_none], obj.get("result"))
        return RetweetedStatusResult(result)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.result is not None:
            result["result"] = from_union([lambda x: to_class(RetweetedStatusResultResult, x), from_none], self.result)
        return result


@dataclass
class FluffyLegacy:
    bookmark_count: Optional[int] = None
    bookmarked: Optional[bool] = None
    created_at: Optional[str] = None
    conversation_id_str: Optional[str] = None
    display_text_range: Optional[List[int]] = None
    entities: Optional[FluffyEntities] = None
    favorite_count: Optional[int] = None
    favorited: Optional[bool] = None
    full_text: Optional[str] = None
    in_reply_to_screen_name: Optional[ScreenName] = None
    in_reply_to_status_id_str: Optional[str] = None
    in_reply_to_user_id_str: Optional[str] = None
    is_quote_status: Optional[bool] = None
    lang: Optional[Lang] = None
    quote_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None
    retweeted: Optional[bool] = None
    user_id_str: Optional[str] = None
    id_str: Optional[str] = None
    self_thread: Optional[SelfThread] = None
    possibly_sensitive: Optional[bool] = None
    possibly_sensitive_editable: Optional[bool] = None
    retweeted_status_result: Optional[RetweetedStatusResult] = None
    quoted_status_id_str: Optional[str] = None
    quoted_status_permalink: Optional[QuotedStatusPermalink] = None
    extended_entities: Optional[PurpleExtendedEntities] = None

    @staticmethod
    def from_dict(obj: Any) -> 'FluffyLegacy':
        assert isinstance(obj, dict)
        bookmark_count = from_union([from_int, from_none], obj.get("bookmark_count"))
        bookmarked = from_union([from_bool, from_none], obj.get("bookmarked"))
        created_at = from_union([from_str, from_none], obj.get("created_at"))
        conversation_id_str = from_union([from_str, from_none], obj.get("conversation_id_str"))
        display_text_range = from_union([lambda x: from_list(from_int, x), from_none], obj.get("display_text_range"))
        entities = from_union([FluffyEntities.from_dict, from_none], obj.get("entities"))
        favorite_count = from_union([from_int, from_none], obj.get("favorite_count"))
        favorited = from_union([from_bool, from_none], obj.get("favorited"))
        full_text = from_union([from_str, from_none], obj.get("full_text"))
        in_reply_to_screen_name = from_union([ScreenName, from_none], obj.get("in_reply_to_screen_name"))
        in_reply_to_status_id_str = from_union([from_str, from_none], obj.get("in_reply_to_status_id_str"))
        in_reply_to_user_id_str = from_union([from_str, from_none], obj.get("in_reply_to_user_id_str"))
        is_quote_status = from_union([from_bool, from_none], obj.get("is_quote_status"))
        lang = from_union([Lang, from_none], obj.get("lang"))
        quote_count = from_union([from_int, from_none], obj.get("quote_count"))
        reply_count = from_union([from_int, from_none], obj.get("reply_count"))
        retweet_count = from_union([from_int, from_none], obj.get("retweet_count"))
        retweeted = from_union([from_bool, from_none], obj.get("retweeted"))
        user_id_str = from_union([from_str, from_none], obj.get("user_id_str"))
        id_str = from_union([from_str, from_none], obj.get("id_str"))
        self_thread = from_union([SelfThread.from_dict, from_none], obj.get("self_thread"))
        possibly_sensitive = from_union([from_bool, from_none], obj.get("possibly_sensitive"))
        possibly_sensitive_editable = from_union([from_bool, from_none], obj.get("possibly_sensitive_editable"))
        retweeted_status_result = from_union([RetweetedStatusResult.from_dict, from_none], obj.get("retweeted_status_result"))
        quoted_status_id_str = from_union([from_str, from_none], obj.get("quoted_status_id_str"))
        quoted_status_permalink = from_union([QuotedStatusPermalink.from_dict, from_none], obj.get("quoted_status_permalink"))
        extended_entities = from_union([PurpleExtendedEntities.from_dict, from_none], obj.get("extended_entities"))
        return FluffyLegacy(bookmark_count, bookmarked, created_at, conversation_id_str, display_text_range, entities, favorite_count, favorited, full_text, in_reply_to_screen_name, in_reply_to_status_id_str, in_reply_to_user_id_str, is_quote_status, lang, quote_count, reply_count, retweet_count, retweeted, user_id_str, id_str, self_thread, possibly_sensitive, possibly_sensitive_editable, retweeted_status_result, quoted_status_id_str, quoted_status_permalink, extended_entities)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.bookmark_count is not None:
            result["bookmark_count"] = from_union([from_int, from_none], self.bookmark_count)
        if self.bookmarked is not None:
            result["bookmarked"] = from_union([from_bool, from_none], self.bookmarked)
        if self.created_at is not None:
            result["created_at"] = from_union([from_str, from_none], self.created_at)
        if self.conversation_id_str is not None:
            result["conversation_id_str"] = from_union([from_str, from_none], self.conversation_id_str)
        if self.display_text_range is not None:
            result["display_text_range"] = from_union([lambda x: from_list(from_int, x), from_none], self.display_text_range)
        if self.entities is not None:
            result["entities"] = from_union([lambda x: to_class(FluffyEntities, x), from_none], self.entities)
        if self.favorite_count is not None:
            result["favorite_count"] = from_union([from_int, from_none], self.favorite_count)
        if self.favorited is not None:
            result["favorited"] = from_union([from_bool, from_none], self.favorited)
        if self.full_text is not None:
            result["full_text"] = from_union([from_str, from_none], self.full_text)
        if self.in_reply_to_screen_name is not None:
            result["in_reply_to_screen_name"] = from_union([lambda x: to_enum(ScreenName, x), from_none], self.in_reply_to_screen_name)
        if self.in_reply_to_status_id_str is not None:
            result["in_reply_to_status_id_str"] = from_union([from_str, from_none], self.in_reply_to_status_id_str)
        if self.in_reply_to_user_id_str is not None:
            result["in_reply_to_user_id_str"] = from_union([from_str, from_none], self.in_reply_to_user_id_str)
        if self.is_quote_status is not None:
            result["is_quote_status"] = from_union([from_bool, from_none], self.is_quote_status)
        if self.lang is not None:
            result["lang"] = from_union([lambda x: to_enum(Lang, x), from_none], self.lang)
        if self.quote_count is not None:
            result["quote_count"] = from_union([from_int, from_none], self.quote_count)
        if self.reply_count is not None:
            result["reply_count"] = from_union([from_int, from_none], self.reply_count)
        if self.retweet_count is not None:
            result["retweet_count"] = from_union([from_int, from_none], self.retweet_count)
        if self.retweeted is not None:
            result["retweeted"] = from_union([from_bool, from_none], self.retweeted)
        if self.user_id_str is not None:
            result["user_id_str"] = from_union([from_str, from_none], self.user_id_str)
        if self.id_str is not None:
            result["id_str"] = from_union([from_str, from_none], self.id_str)
        if self.self_thread is not None:
            result["self_thread"] = from_union([lambda x: to_class(SelfThread, x), from_none], self.self_thread)
        if self.possibly_sensitive is not None:
            result["possibly_sensitive"] = from_union([from_bool, from_none], self.possibly_sensitive)
        if self.possibly_sensitive_editable is not None:
            result["possibly_sensitive_editable"] = from_union([from_bool, from_none], self.possibly_sensitive_editable)
        if self.retweeted_status_result is not None:
            result["retweeted_status_result"] = from_union([lambda x: to_class(RetweetedStatusResult, x), from_none], self.retweeted_status_result)
        if self.quoted_status_id_str is not None:
            result["quoted_status_id_str"] = from_union([from_str, from_none], self.quoted_status_id_str)
        if self.quoted_status_permalink is not None:
            result["quoted_status_permalink"] = from_union([lambda x: to_class(QuotedStatusPermalink, x), from_none], self.quoted_status_permalink)
        if self.extended_entities is not None:
            result["extended_entities"] = from_union([lambda x: to_class(PurpleExtendedEntities, x), from_none], self.extended_entities)
        return result


class Eligibility(Enum):
    INELIGIBLE_USER_UNAUTHORIZED = "IneligibleUserUnauthorized"


@dataclass
class QuickPromoteEligibility:
    eligibility: Optional[Eligibility] = None

    @staticmethod
    def from_dict(obj: Any) -> 'QuickPromoteEligibility':
        assert isinstance(obj, dict)
        eligibility = from_union([Eligibility, from_none], obj.get("eligibility"))
        return QuickPromoteEligibility(eligibility)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.eligibility is not None:
            result["eligibility"] = from_union([lambda x: to_enum(Eligibility, x), from_none], self.eligibility)
        return result


@dataclass
class UnifiedCard:
    card_fetch_state: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'UnifiedCard':
        assert isinstance(obj, dict)
        card_fetch_state = from_union([from_str, from_none], obj.get("card_fetch_state"))
        return UnifiedCard(card_fetch_state)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.card_fetch_state is not None:
            result["card_fetch_state"] = from_union([from_str, from_none], self.card_fetch_state)
        return result


@dataclass
class TweetResultsResult:
    typename: Optional[TweetDisplayType] = None
    rest_id: Optional[str] = None
    has_birdwatch_notes: Optional[bool] = None
    core: Optional[Core] = None
    unmention_data: Optional[UnmentionData] = None
    edit_control: Optional[EditControl] = None
    is_translatable: Optional[bool] = None
    views: Optional[Views] = None
    source: Optional[str] = None
    legacy: Optional[FluffyLegacy] = None
    quick_promote_eligibility: Optional[QuickPromoteEligibility] = None
    card: Optional[Card] = None
    unified_card: Optional[UnifiedCard] = None
    quoted_status_result: Optional[QuotedStatusResult] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TweetResultsResult':
        assert isinstance(obj, dict)
        typename = from_union([TweetDisplayType, from_none], obj.get("__typename"))
        rest_id = from_union([from_str, from_none], obj.get("rest_id"))
        has_birdwatch_notes = from_union([from_bool, from_none], obj.get("has_birdwatch_notes"))
        core = from_union([Core.from_dict, from_none], obj.get("core"))
        unmention_data = from_union([UnmentionData.from_dict, from_none], obj.get("unmention_data"))
        edit_control = from_union([EditControl.from_dict, from_none], obj.get("edit_control"))
        is_translatable = from_union([from_bool, from_none], obj.get("is_translatable"))
        views = from_union([Views.from_dict, from_none], obj.get("views"))
        source = from_union([from_str, from_none], obj.get("source"))
        legacy = from_union([FluffyLegacy.from_dict, from_none], obj.get("legacy"))
        quick_promote_eligibility = from_union([QuickPromoteEligibility.from_dict, from_none], obj.get("quick_promote_eligibility"))
        card = from_union([Card.from_dict, from_none], obj.get("card"))
        unified_card = from_union([UnifiedCard.from_dict, from_none], obj.get("unified_card"))
        quoted_status_result = from_union([QuotedStatusResult.from_dict, from_none], obj.get("quoted_status_result"))
        return TweetResultsResult(typename, rest_id, has_birdwatch_notes, core, unmention_data, edit_control, is_translatable, views, source, legacy, quick_promote_eligibility, card, unified_card, quoted_status_result)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.typename is not None:
            result["__typename"] = from_union([lambda x: to_enum(TweetDisplayType, x), from_none], self.typename)
        if self.rest_id is not None:
            result["rest_id"] = from_union([from_str, from_none], self.rest_id)
        if self.has_birdwatch_notes is not None:
            result["has_birdwatch_notes"] = from_union([from_bool, from_none], self.has_birdwatch_notes)
        if self.core is not None:
            result["core"] = from_union([lambda x: to_class(Core, x), from_none], self.core)
        if self.unmention_data is not None:
            result["unmention_data"] = from_union([lambda x: to_class(UnmentionData, x), from_none], self.unmention_data)
        if self.edit_control is not None:
            result["edit_control"] = from_union([lambda x: to_class(EditControl, x), from_none], self.edit_control)
        if self.is_translatable is not None:
            result["is_translatable"] = from_union([from_bool, from_none], self.is_translatable)
        if self.views is not None:
            result["views"] = from_union([lambda x: to_class(Views, x), from_none], self.views)
        if self.source is not None:
            result["source"] = from_union([from_str, from_none], self.source)
        if self.legacy is not None:
            result["legacy"] = from_union([lambda x: to_class(FluffyLegacy, x), from_none], self.legacy)
        if self.quick_promote_eligibility is not None:
            result["quick_promote_eligibility"] = from_union([lambda x: to_class(QuickPromoteEligibility, x), from_none], self.quick_promote_eligibility)
        if self.card is not None:
            result["card"] = from_union([lambda x: to_class(Card, x), from_none], self.card)
        if self.unified_card is not None:
            result["unified_card"] = from_union([lambda x: to_class(UnifiedCard, x), from_none], self.unified_card)
        if self.quoted_status_result is not None:
            result["quoted_status_result"] = from_union([lambda x: to_class(QuotedStatusResult, x), from_none], self.quoted_status_result)
        return result


@dataclass
class TweetResults:
    result: Optional[TweetResultsResult] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TweetResults':
        assert isinstance(obj, dict)
        result = from_union([TweetResultsResult.from_dict, from_none], obj.get("result"))
        return TweetResults(result)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.result is not None:
            result["result"] = from_union([lambda x: to_class(TweetResultsResult, x), from_none], self.result)
        return result


@dataclass
class ItemContent:
    item_type: Optional[ItemTypeEnum] = None
    typename: Optional[ItemTypeEnum] = None
    tweet_results: Optional[TweetResults] = None
    tweet_display_type: Optional[TweetDisplayType] = None
    rux_context: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ItemContent':
        assert isinstance(obj, dict)
        item_type = from_union([ItemTypeEnum, from_none], obj.get("itemType"))
        typename = from_union([ItemTypeEnum, from_none], obj.get("__typename"))
        tweet_results = from_union([TweetResults.from_dict, from_none], obj.get("tweet_results"))
        tweet_display_type = from_union([TweetDisplayType, from_none], obj.get("tweetDisplayType"))
        rux_context = from_union([from_str, from_none], obj.get("ruxContext"))
        return ItemContent(item_type, typename, tweet_results, tweet_display_type, rux_context)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.item_type is not None:
            result["itemType"] = from_union([lambda x: to_enum(ItemTypeEnum, x), from_none], self.item_type)
        if self.typename is not None:
            result["__typename"] = from_union([lambda x: to_enum(ItemTypeEnum, x), from_none], self.typename)
        if self.tweet_results is not None:
            result["tweet_results"] = from_union([lambda x: to_class(TweetResults, x), from_none], self.tweet_results)
        if self.tweet_display_type is not None:
            result["tweetDisplayType"] = from_union([lambda x: to_enum(TweetDisplayType, x), from_none], self.tweet_display_type)
        if self.rux_context is not None:
            result["ruxContext"] = from_union([from_str, from_none], self.rux_context)
        return result


@dataclass
class Content:
    entry_type: Optional[EntryTypeEnum] = None
    typename: Optional[EntryTypeEnum] = None
    item_content: Optional[ItemContent] = None
    value: Optional[str] = None
    cursor_type: Optional[CursorType] = None
    stop_on_empty_response: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Content':
        assert isinstance(obj, dict)
        entry_type = from_union([EntryTypeEnum, from_none], obj.get("entryType"))
        typename = from_union([EntryTypeEnum, from_none], obj.get("__typename"))
        item_content = from_union([ItemContent.from_dict, from_none], obj.get("itemContent"))
        value = from_union([from_str, from_none], obj.get("value"))
        cursor_type = from_union([CursorType, from_none], obj.get("cursorType"))
        stop_on_empty_response = from_union([from_bool, from_none], obj.get("stopOnEmptyResponse"))
        return Content(entry_type, typename, item_content, value, cursor_type, stop_on_empty_response)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.entry_type is not None:
            result["entryType"] = from_union([lambda x: to_enum(EntryTypeEnum, x), from_none], self.entry_type)
        if self.typename is not None:
            result["__typename"] = from_union([lambda x: to_enum(EntryTypeEnum, x), from_none], self.typename)
        if self.item_content is not None:
            result["itemContent"] = from_union([lambda x: to_class(ItemContent, x), from_none], self.item_content)
        if self.value is not None:
            result["value"] = from_union([from_str, from_none], self.value)
        if self.cursor_type is not None:
            result["cursorType"] = from_union([lambda x: to_enum(CursorType, x), from_none], self.cursor_type)
        if self.stop_on_empty_response is not None:
            result["stopOnEmptyResponse"] = from_union([from_bool, from_none], self.stop_on_empty_response)
        return result


@dataclass
class Entry:
    entry_id: Optional[str] = None
    sort_index: Optional[str] = None
    content: Optional[Content] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Entry':
        assert isinstance(obj, dict)
        entry_id = from_union([from_str, from_none], obj.get("entryId"))
        sort_index = from_union([from_str, from_none], obj.get("sortIndex"))
        content = from_union([Content.from_dict, from_none], obj.get("content"))
        return Entry(entry_id, sort_index, content)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.entry_id is not None:
            result["entryId"] = from_union([from_str, from_none], self.entry_id)
        if self.sort_index is not None:
            result["sortIndex"] = from_union([from_str, from_none], self.sort_index)
        if self.content is not None:
            result["content"] = from_union([lambda x: to_class(Content, x), from_none], self.content)
        return result


class InstructionType(Enum):
    TIMELINE_ADD_ENTRIES = "TimelineAddEntries"
    TIMELINE_CLEAR_CACHE = "TimelineClearCache"


@dataclass
class Instruction:
    type: Optional[InstructionType] = None
    entries: Optional[List[Entry]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Instruction':
        assert isinstance(obj, dict)
        type = from_union([InstructionType, from_none], obj.get("type"))
        entries = from_union([lambda x: from_list(Entry.from_dict, x), from_none], obj.get("entries"))
        return Instruction(type, entries)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.type is not None:
            result["type"] = from_union([lambda x: to_enum(InstructionType, x), from_none], self.type)
        if self.entries is not None:
            result["entries"] = from_union([lambda x: from_list(lambda x: to_class(Entry, x), x), from_none], self.entries)
        return result


@dataclass
class ResponseObjects:
    feedback_actions: Optional[List[Any]] = None
    immediate_reactions: Optional[List[Any]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ResponseObjects':
        assert isinstance(obj, dict)
        feedback_actions = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("feedbackActions"))
        immediate_reactions = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("immediateReactions"))
        return ResponseObjects(feedback_actions, immediate_reactions)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.feedback_actions is not None:
            result["feedbackActions"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.feedback_actions)
        if self.immediate_reactions is not None:
            result["immediateReactions"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.immediate_reactions)
        return result


@dataclass
class Timeline:
    instructions: Optional[List[Instruction]] = None
    response_objects: Optional[ResponseObjects] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Timeline':
        assert isinstance(obj, dict)
        instructions = from_union([lambda x: from_list(Instruction.from_dict, x), from_none], obj.get("instructions"))
        response_objects = from_union([ResponseObjects.from_dict, from_none], obj.get("responseObjects"))
        return Timeline(instructions, response_objects)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.instructions is not None:
            result["instructions"] = from_union([lambda x: from_list(lambda x: to_class(Instruction, x), x), from_none], self.instructions)
        if self.response_objects is not None:
            result["responseObjects"] = from_union([lambda x: to_class(ResponseObjects, x), from_none], self.response_objects)
        return result


@dataclass
class TimelineV2:
    timeline: Optional[Timeline] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TimelineV2':
        assert isinstance(obj, dict)
        timeline = from_union([Timeline.from_dict, from_none], obj.get("timeline"))
        return TimelineV2(timeline)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.timeline is not None:
            result["timeline"] = from_union([lambda x: to_class(Timeline, x), from_none], self.timeline)
        return result


@dataclass
class UserResult:
    typename: Optional[Typename] = None
    timeline_v2: Optional[TimelineV2] = None

    @staticmethod
    def from_dict(obj: Any) -> 'UserResult':
        assert isinstance(obj, dict)
        typename = from_union([Typename, from_none], obj.get("__typename"))
        timeline_v2 = from_union([TimelineV2.from_dict, from_none], obj.get("timeline_v2"))
        return UserResult(typename, timeline_v2)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.typename is not None:
            result["__typename"] = from_union([lambda x: to_enum(Typename, x), from_none], self.typename)
        if self.timeline_v2 is not None:
            result["timeline_v2"] = from_union([lambda x: to_class(TimelineV2, x), from_none], self.timeline_v2)
        return result


@dataclass
class User:
    result: Optional[UserResult] = None

    @staticmethod
    def from_dict(obj: Any) -> 'User':
        assert isinstance(obj, dict)
        result = from_union([UserResult.from_dict, from_none], obj.get("result"))
        return User(result)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.result is not None:
            result["result"] = from_union([lambda x: to_class(UserResult, x), from_none], self.result)
        return result


@dataclass
class Data:
    user: Optional[User] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        user = from_union([User.from_dict, from_none], obj.get("user"))
        return Data(user)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.user is not None:
            result["user"] = from_union([lambda x: to_class(User, x), from_none], self.user)
        return result


@dataclass
class TwitterDatum:
    data: Optional[Data] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TwitterDatum':
        assert isinstance(obj, dict)
        data = from_union([Data.from_dict, from_none], obj.get("data"))
        return TwitterDatum(data)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.data is not None:
            result["data"] = from_union([lambda x: to_class(Data, x), from_none], self.data)
        return result


def twitter_data_from_dict(s: Any) -> List[List[TwitterDatum]]:
    return from_list(lambda x: from_list(TwitterDatum.from_dict, x), s)


def twitter_data_to_dict(x: List[List[TwitterDatum]]) -> Any:
    return from_list(lambda x: from_list(lambda x: to_class(TwitterDatum, x), x), x)
