from enum import Enum
from dataclasses import dataclass
from typing import Optional, Any, List, TypeVar, Type, cast, Callable


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


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


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def is_type(t: Type[T], x: Any) -> T:
    assert isinstance(x, t)
    return x


class Ent(Enum):
    SUGGEST_RANKED_ORGANIC_TWEET = "suggest_ranked_organic_tweet"
    SUGGEST_WHO_TO_FOLLOW = "suggest_who_to_follow"
    TWEET = "tweet"


class ControllerData(Enum):
    DAACDAABDAAB_CG_ABAAAAAAAAAAAKA_AK_P_DU_DAB9_AG_AAAAAAA = "DAACDAABDAABCgABAAAAAAAAAAAKAAkPDuDab9agAAAAAAA="
    DAACDAACDAAB_CG_ABAAAAAAAAA_AG_AAAAA = "DAACDAACDAABCgABAAAAAAAAAAgAAAAA"


class InjectionType(Enum):
    RANKED_ORGANIC_TWEET = "RankedOrganicTweet"
    WHO_TO_FOLLOW = "WhoToFollow"


@dataclass
class TimelinesDetails:
    injection_type: Optional[InjectionType] = None
    controller_data: Optional[ControllerData] = None
    source_data: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TimelinesDetails':
        assert isinstance(obj, dict)
        injection_type = from_union([InjectionType, from_none], obj.get("injectionType"))
        controller_data = from_union([ControllerData, from_none], obj.get("controllerData"))
        source_data = from_union([from_str, from_none], obj.get("sourceData"))
        return TimelinesDetails(injection_type, controller_data, source_data)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.injection_type is not None:
            result["injectionType"] = from_union([lambda x: to_enum(InjectionType, x), from_none], self.injection_type)
        if self.controller_data is not None:
            result["controllerData"] = from_union([lambda x: to_enum(ControllerData, x), from_none], self.controller_data)
        if self.source_data is not None:
            result["sourceData"] = from_union([from_str, from_none], self.source_data)
        return result


@dataclass
class Details:
    timelines_details: Optional[TimelinesDetails] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Details':
        assert isinstance(obj, dict)
        timelines_details = from_union([TimelinesDetails.from_dict, from_none], obj.get("timelinesDetails"))
        return Details(timelines_details)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.timelines_details is not None:
            result["timelinesDetails"] = from_union([lambda x: to_class(TimelinesDetails, x), from_none], self.timelines_details)
        return result


@dataclass
class ContentClientEventInfo:
    component: Optional[Ent] = None
    element: Optional[Ent] = None
    details: Optional[Details] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ContentClientEventInfo':
        assert isinstance(obj, dict)
        component = from_union([Ent, from_none], obj.get("component"))
        element = from_union([Ent, from_none], obj.get("element"))
        details = from_union([Details.from_dict, from_none], obj.get("details"))
        return ContentClientEventInfo(component, element, details)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.component is not None:
            result["component"] = from_union([lambda x: to_enum(Ent, x), from_none], self.component)
        if self.element is not None:
            result["element"] = from_union([lambda x: to_enum(Ent, x), from_none], self.element)
        if self.details is not None:
            result["details"] = from_union([lambda x: to_class(Details, x), from_none], self.details)
        return result


class CursorType(Enum):
    BOTTOM = "Bottom"
    TOP = "Top"


class DisplayType(Enum):
    VERTICAL = "Vertical"
    VERTICAL_CONVERSATION = "VerticalConversation"


class EntryTypeEnum(Enum):
    TIMELINE_TIMELINE_CURSOR = "TimelineTimelineCursor"
    TIMELINE_TIMELINE_ITEM = "TimelineTimelineItem"
    TIMELINE_TIMELINE_MODULE = "TimelineTimelineModule"


@dataclass
class LandingURL:
    url: Optional[str] = None
    url_type: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'LandingURL':
        assert isinstance(obj, dict)
        url = from_union([from_str, from_none], obj.get("url"))
        url_type = from_union([from_str, from_none], obj.get("urlType"))
        return LandingURL(url, url_type)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.url is not None:
            result["url"] = from_union([from_str, from_none], self.url)
        if self.url_type is not None:
            result["urlType"] = from_union([from_str, from_none], self.url_type)
        return result


@dataclass
class Footer:
    display_type: Optional[str] = None
    text: Optional[str] = None
    landing_url: Optional[LandingURL] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Footer':
        assert isinstance(obj, dict)
        display_type = from_union([from_str, from_none], obj.get("displayType"))
        text = from_union([from_str, from_none], obj.get("text"))
        landing_url = from_union([LandingURL.from_dict, from_none], obj.get("landingUrl"))
        return Footer(display_type, text, landing_url)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.display_type is not None:
            result["displayType"] = from_union([from_str, from_none], self.display_type)
        if self.text is not None:
            result["text"] = from_union([from_str, from_none], self.text)
        if self.landing_url is not None:
            result["landingUrl"] = from_union([lambda x: to_class(LandingURL, x), from_none], self.landing_url)
        return result


@dataclass
class Header:
    display_type: Optional[str] = None
    text: Optional[str] = None
    sticky: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Header':
        assert isinstance(obj, dict)
        display_type = from_union([from_str, from_none], obj.get("displayType"))
        text = from_union([from_str, from_none], obj.get("text"))
        sticky = from_union([from_bool, from_none], obj.get("sticky"))
        return Header(display_type, text, sticky)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.display_type is not None:
            result["displayType"] = from_union([from_str, from_none], self.display_type)
        if self.text is not None:
            result["text"] = from_union([from_str, from_none], self.text)
        if self.sticky is not None:
            result["sticky"] = from_union([from_bool, from_none], self.sticky)
        return result


class ItemTypeEnum(Enum):
    TIMELINE_TWEET = "TimelineTweet"
    TIMELINE_USER = "TimelineUser"


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


@dataclass
class PurpleValue:
    image_value: Optional[ImageValue] = None
    type: Optional[ValueType] = None
    string_value: Optional[str] = None
    scribe_key: Optional[str] = None
    image_color_value: Optional[ImageColorValue] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PurpleValue':
        assert isinstance(obj, dict)
        image_value = from_union([ImageValue.from_dict, from_none], obj.get("image_value"))
        type = from_union([ValueType, from_none], obj.get("type"))
        string_value = from_union([from_str, from_none], obj.get("string_value"))
        scribe_key = from_union([from_str, from_none], obj.get("scribe_key"))
        image_color_value = from_union([ImageColorValue.from_dict, from_none], obj.get("image_color_value"))
        return PurpleValue(image_value, type, string_value, scribe_key, image_color_value)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.image_value is not None:
            result["image_value"] = from_union([lambda x: to_class(ImageValue, x), from_none], self.image_value)
        if self.type is not None:
            result["type"] = from_union([lambda x: to_enum(ValueType, x), from_none], self.type)
        if self.string_value is not None:
            result["string_value"] = from_union([from_str, from_none], self.string_value)
        if self.scribe_key is not None:
            result["scribe_key"] = from_union([from_str, from_none], self.scribe_key)
        if self.image_color_value is not None:
            result["image_color_value"] = from_union([lambda x: to_class(ImageColorValue, x), from_none], self.image_color_value)
        return result


@dataclass
class PurpleBindingValue:
    key: Optional[str] = None
    value: Optional[PurpleValue] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PurpleBindingValue':
        assert isinstance(obj, dict)
        key = from_union([from_str, from_none], obj.get("key"))
        value = from_union([PurpleValue.from_dict, from_none], obj.get("value"))
        return PurpleBindingValue(key, value)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.key is not None:
            result["key"] = from_union([from_str, from_none], self.key)
        if self.value is not None:
            result["value"] = from_union([lambda x: to_class(PurpleValue, x), from_none], self.value)
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
class PurpleLegacy:
    binding_values: Optional[List[PurpleBindingValue]] = None
    card_platform: Optional[CardPlatform] = None
    name: Optional[str] = None
    url: Optional[str] = None
    user_refs_results: Optional[List[Any]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PurpleLegacy':
        assert isinstance(obj, dict)
        binding_values = from_union([lambda x: from_list(PurpleBindingValue.from_dict, x), from_none], obj.get("binding_values"))
        card_platform = from_union([CardPlatform.from_dict, from_none], obj.get("card_platform"))
        name = from_union([from_str, from_none], obj.get("name"))
        url = from_union([from_str, from_none], obj.get("url"))
        user_refs_results = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("user_refs_results"))
        return PurpleLegacy(binding_values, card_platform, name, url, user_refs_results)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.binding_values is not None:
            result["binding_values"] = from_union([lambda x: from_list(lambda x: to_class(PurpleBindingValue, x), x), from_none], self.binding_values)
        if self.card_platform is not None:
            result["card_platform"] = from_union([lambda x: to_class(CardPlatform, x), from_none], self.card_platform)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.url is not None:
            result["url"] = from_union([from_str, from_none], self.url)
        if self.user_refs_results is not None:
            result["user_refs_results"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.user_refs_results)
        return result


@dataclass
class PurpleCard:
    rest_id: Optional[str] = None
    legacy: Optional[PurpleLegacy] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PurpleCard':
        assert isinstance(obj, dict)
        rest_id = from_union([from_str, from_none], obj.get("rest_id"))
        legacy = from_union([PurpleLegacy.from_dict, from_none], obj.get("legacy"))
        return PurpleCard(rest_id, legacy)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.rest_id is not None:
            result["rest_id"] = from_union([from_str, from_none], self.rest_id)
        if self.legacy is not None:
            result["legacy"] = from_union([lambda x: to_class(PurpleLegacy, x), from_none], self.legacy)
        return result


@dataclass
class AffiliatesHighlightedLabel:
    pass

    @staticmethod
    def from_dict(obj: Any) -> 'AffiliatesHighlightedLabel':
        assert isinstance(obj, dict)
        return AffiliatesHighlightedLabel()

    def to_dict(self) -> dict:
        result: dict = {}
        return result


class ID(Enum):
    VX_NLCJO0_MJ_IZ_MT_YY_NA = "VXNlcjo0MjIzMTYyNA=="
    VX_NLCJO3_MD_UZ_NZ_UX_MTQ4_MJK4_O_DK1_MZ_Y = "VXNlcjo3MDUzNzUxMTQ4Mjk4ODk1MzY="
    VX_NLCJO5_MT_YY_MTU2_M_TG2_MTI5_NZ_M1_NJG = "VXNlcjo5MTYyMTU2MTg2MTI5NzM1Njg="
    VX_NLCJOX_MDA1_ODI2_ODM2 = "VXNlcjoxMDA1ODI2ODM2"
    VX_NLCJOX_MJ_Q4_ND_EX_OT_YW = "VXNlcjoxMjQ4NDExOTYw"
    VX_NLCJOX_NDY5_MZ_A4_MDA4 = "VXNlcjoxNDY5MzA4MDA4"
    VX_NLCJOY_M_TK3_NZ_AX_NDA1 = "VXNlcjoyMTk3NzAxNDA1"
    VX_NLCJOY_M_TKX_N_DC4_ODQ5 = "VXNlcjoyMTkxNDc4ODQ5"


class CreatedAt(Enum):
    FRI_NOV_2215382100002013 = "Fri Nov 22 15:38:21 +0000 2013"
    FRI_OCT_0608164000002017 = "Fri Oct 06 08:16:40 +0000 2017"
    SUN_MAY_2415530600002009 = "Sun May 24 15:53:06 +0000 2009"
    THU_MAR_0312514700002016 = "Thu Mar 03 12:51:47 +0000 2016"
    THU_MAR_0710285200002013 = "Thu Mar 07 10:28:52 +0000 2013"
    THU_MAY_3009213800002013 = "Thu May 30 09:21:38 +0000 2013"
    WED_DEC_1207552000002012 = "Wed Dec 12 07:55:20 +0000 2012"
    WED_NOV_2709155500002013 = "Wed Nov 27 09:15:55 +0000 2013"


@dataclass
class PurpleDescription:
    urls: Optional[List[Any]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PurpleDescription':
        assert isinstance(obj, dict)
        urls = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("urls"))
        return PurpleDescription(urls)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.urls is not None:
            result["urls"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.urls)
        return result


class DisplayURL(Enum):
    BERGEN_KOMMUNE_NO_BRANNVESEN = "bergen-kommune.no/brannvesen"
    DMI_DK = "dmi.dk"
    HOVEDREDNINGSSENTRALEN_NO = "hovedredningssentralen.no"
    POLITIET_NO = "politiet.no"
    POLITIET_NO_SORVEST = "politiet.no/sorvest"
    ROGBR_NO = "rogbr.no"
    VEGVESEN_NO_TRAFIKKINFORMA = "vegvesen.no/Trafikkinforma…"
    YR_NO = "yr.no"


@dataclass
class FluffyURL:
    display_url: Optional[DisplayURL] = None
    expanded_url: Optional[str] = None
    url: Optional[str] = None
    indices: Optional[List[int]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'FluffyURL':
        assert isinstance(obj, dict)
        display_url = from_union([DisplayURL, from_none], obj.get("display_url"))
        expanded_url = from_union([from_str, from_none], obj.get("expanded_url"))
        url = from_union([from_str, from_none], obj.get("url"))
        indices = from_union([lambda x: from_list(from_int, x), from_none], obj.get("indices"))
        return FluffyURL(display_url, expanded_url, url, indices)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.display_url is not None:
            result["display_url"] = from_union([lambda x: to_enum(DisplayURL, x), from_none], self.display_url)
        if self.expanded_url is not None:
            result["expanded_url"] = from_union([from_str, from_none], self.expanded_url)
        if self.url is not None:
            result["url"] = from_union([from_str, from_none], self.url)
        if self.indices is not None:
            result["indices"] = from_union([lambda x: from_list(from_int, x), from_none], self.indices)
        return result


@dataclass
class PurpleURL:
    urls: Optional[List[FluffyURL]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PurpleURL':
        assert isinstance(obj, dict)
        urls = from_union([lambda x: from_list(FluffyURL.from_dict, x), from_none], obj.get("urls"))
        return PurpleURL(urls)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.urls is not None:
            result["urls"] = from_union([lambda x: from_list(lambda x: to_class(FluffyURL, x), x), from_none], self.urls)
        return result


@dataclass
class PurpleEntities:
    description: Optional[PurpleDescription] = None
    url: Optional[PurpleURL] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PurpleEntities':
        assert isinstance(obj, dict)
        description = from_union([PurpleDescription.from_dict, from_none], obj.get("description"))
        url = from_union([PurpleURL.from_dict, from_none], obj.get("url"))
        return PurpleEntities(description, url)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.description is not None:
            result["description"] = from_union([lambda x: to_class(PurpleDescription, x), from_none], self.description)
        if self.url is not None:
            result["url"] = from_union([lambda x: to_class(PurpleURL, x), from_none], self.url)
        return result


class Location(Enum):
    BERGEN_NORGE = "Bergen, Norge"
    COPENHAGEN_DENMARK = "Copenhagen, Denmark"
    EMPTY = ""
    MONS_NORWAY = "Mons, Norway"
    NORGE = "Norge"
    ROGALAND_BRANN_OG_REDNING_IKS = "Rogaland brann og redning IKS"
    VESTLAND_FYLKE = "Vestland fylke"


class Name(Enum):
    DMI = "DMI"
    HRS_SØR_NORGE = "HRS Sør-Norge"
    METEOROLOGENE = "Meteorologene"
    POLITIET_I_SØR_VEST = "Politiet i Sør-Vest"
    THE_110_SØR_VEST = "110 Sør-Vest"
    THE_110_VEST = "110 Vest"
    VEGTRAFIKKSENTRALEN_VEST = "Vegtrafikksentralen vest"
    VEST_POLITIDISTRIKT = "Vest politidistrikt"


class ScreenName(Enum):
    DMIDK = "dmidk"
    HRS_SOR_NORGE = "HRSSorNorge"
    METEOROLOGENE = "Meteorologene"
    POLITIETSORVEST = "politietsorvest"
    POLITIVEST = "politivest"
    THE_110_SOR_VEST = "110SorVest"
    THE_110_VEST = "110Vest"
    VT_SVEST = "VTSvest"


class TranslatorType(Enum):
    NONE = "none"


@dataclass
class FluffyLegacy:
    can_dm: Optional[bool] = None
    can_media_tag: Optional[bool] = None
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
    pinned_tweet_ids_str: Optional[List[Any]] = None
    possibly_sensitive: Optional[bool] = None
    profile_image_url_https: Optional[str] = None
    profile_interstitial_type: Optional[str] = None
    screen_name: Optional[ScreenName] = None
    statuses_count: Optional[int] = None
    translator_type: Optional[TranslatorType] = None
    url: Optional[str] = None
    verified: Optional[bool] = None
    want_retweets: Optional[bool] = None
    withheld_in_countries: Optional[List[Any]] = None
    profile_banner_url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'FluffyLegacy':
        assert isinstance(obj, dict)
        can_dm = from_union([from_bool, from_none], obj.get("can_dm"))
        can_media_tag = from_union([from_bool, from_none], obj.get("can_media_tag"))
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
        pinned_tweet_ids_str = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("pinned_tweet_ids_str"))
        possibly_sensitive = from_union([from_bool, from_none], obj.get("possibly_sensitive"))
        profile_image_url_https = from_union([from_str, from_none], obj.get("profile_image_url_https"))
        profile_interstitial_type = from_union([from_str, from_none], obj.get("profile_interstitial_type"))
        screen_name = from_union([ScreenName, from_none], obj.get("screen_name"))
        statuses_count = from_union([from_int, from_none], obj.get("statuses_count"))
        translator_type = from_union([TranslatorType, from_none], obj.get("translator_type"))
        url = from_union([from_str, from_none], obj.get("url"))
        verified = from_union([from_bool, from_none], obj.get("verified"))
        want_retweets = from_union([from_bool, from_none], obj.get("want_retweets"))
        withheld_in_countries = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("withheld_in_countries"))
        profile_banner_url = from_union([from_str, from_none], obj.get("profile_banner_url"))
        return FluffyLegacy(can_dm, can_media_tag, created_at, default_profile, default_profile_image, description, entities, fast_followers_count, favourites_count, followers_count, friends_count, has_custom_timelines, is_translator, listed_count, location, media_count, name, normal_followers_count, pinned_tweet_ids_str, possibly_sensitive, profile_image_url_https, profile_interstitial_type, screen_name, statuses_count, translator_type, url, verified, want_retweets, withheld_in_countries, profile_banner_url)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.can_dm is not None:
            result["can_dm"] = from_union([from_bool, from_none], self.can_dm)
        if self.can_media_tag is not None:
            result["can_media_tag"] = from_union([from_bool, from_none], self.can_media_tag)
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
            result["pinned_tweet_ids_str"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.pinned_tweet_ids_str)
        if self.possibly_sensitive is not None:
            result["possibly_sensitive"] = from_union([from_bool, from_none], self.possibly_sensitive)
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
        if self.want_retweets is not None:
            result["want_retweets"] = from_union([from_bool, from_none], self.want_retweets)
        if self.withheld_in_countries is not None:
            result["withheld_in_countries"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.withheld_in_countries)
        if self.profile_banner_url is not None:
            result["profile_banner_url"] = from_union([from_str, from_none], self.profile_banner_url)
        return result


class ProfileImageShape(Enum):
    CIRCLE = "Circle"


class UserDisplayTypeEnum(Enum):
    USER = "User"


@dataclass
class FluffyResult:
    typename: Optional[UserDisplayTypeEnum] = None
    id: Optional[ID] = None
    rest_id: Optional[str] = None
    affiliates_highlighted_label: Optional[AffiliatesHighlightedLabel] = None
    has_graduated_access: Optional[bool] = None
    is_blue_verified: Optional[bool] = None
    profile_image_shape: Optional[ProfileImageShape] = None
    legacy: Optional[FluffyLegacy] = None
    smart_blocked_by: Optional[bool] = None
    smart_blocking: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'FluffyResult':
        assert isinstance(obj, dict)
        typename = from_union([UserDisplayTypeEnum, from_none], obj.get("__typename"))
        id = from_union([ID, from_none], obj.get("id"))
        rest_id = from_union([from_str, from_none], obj.get("rest_id"))
        affiliates_highlighted_label = from_union([AffiliatesHighlightedLabel.from_dict, from_none], obj.get("affiliates_highlighted_label"))
        has_graduated_access = from_union([from_bool, from_none], obj.get("has_graduated_access"))
        is_blue_verified = from_union([from_bool, from_none], obj.get("is_blue_verified"))
        profile_image_shape = from_union([ProfileImageShape, from_none], obj.get("profile_image_shape"))
        legacy = from_union([FluffyLegacy.from_dict, from_none], obj.get("legacy"))
        smart_blocked_by = from_union([from_bool, from_none], obj.get("smart_blocked_by"))
        smart_blocking = from_union([from_bool, from_none], obj.get("smart_blocking"))
        return FluffyResult(typename, id, rest_id, affiliates_highlighted_label, has_graduated_access, is_blue_verified, profile_image_shape, legacy, smart_blocked_by, smart_blocking)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.typename is not None:
            result["__typename"] = from_union([lambda x: to_enum(UserDisplayTypeEnum, x), from_none], self.typename)
        if self.id is not None:
            result["id"] = from_union([lambda x: to_enum(ID, x), from_none], self.id)
        if self.rest_id is not None:
            result["rest_id"] = from_union([from_str, from_none], self.rest_id)
        if self.affiliates_highlighted_label is not None:
            result["affiliates_highlighted_label"] = from_union([lambda x: to_class(AffiliatesHighlightedLabel, x), from_none], self.affiliates_highlighted_label)
        if self.has_graduated_access is not None:
            result["has_graduated_access"] = from_union([from_bool, from_none], self.has_graduated_access)
        if self.is_blue_verified is not None:
            result["is_blue_verified"] = from_union([from_bool, from_none], self.is_blue_verified)
        if self.profile_image_shape is not None:
            result["profile_image_shape"] = from_union([lambda x: to_enum(ProfileImageShape, x), from_none], self.profile_image_shape)
        if self.legacy is not None:
            result["legacy"] = from_union([lambda x: to_class(FluffyLegacy, x), from_none], self.legacy)
        if self.smart_blocked_by is not None:
            result["smart_blocked_by"] = from_union([from_bool, from_none], self.smart_blocked_by)
        if self.smart_blocking is not None:
            result["smart_blocking"] = from_union([from_bool, from_none], self.smart_blocking)
        return result


@dataclass
class PurpleUserResults:
    result: Optional[FluffyResult] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PurpleUserResults':
        assert isinstance(obj, dict)
        result = from_union([FluffyResult.from_dict, from_none], obj.get("result"))
        return PurpleUserResults(result)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.result is not None:
            result["result"] = from_union([lambda x: to_class(FluffyResult, x), from_none], self.result)
        return result


@dataclass
class PurpleCore:
    user_results: Optional[PurpleUserResults] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PurpleCore':
        assert isinstance(obj, dict)
        user_results = from_union([PurpleUserResults.from_dict, from_none], obj.get("user_results"))
        return PurpleCore(user_results)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.user_results is not None:
            result["user_results"] = from_union([lambda x: to_class(PurpleUserResults, x), from_none], self.user_results)
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
class EditPerspective:
    favorited: Optional[bool] = None
    retweeted: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'EditPerspective':
        assert isinstance(obj, dict)
        favorited = from_union([from_bool, from_none], obj.get("favorited"))
        retweeted = from_union([from_bool, from_none], obj.get("retweeted"))
        return EditPerspective(favorited, retweeted)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.favorited is not None:
            result["favorited"] = from_union([from_bool, from_none], self.favorited)
        if self.retweeted is not None:
            result["retweeted"] = from_union([from_bool, from_none], self.retweeted)
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
class PurpleLarge:
    faces: Optional[List[FocusRect]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PurpleLarge':
        assert isinstance(obj, dict)
        faces = from_union([lambda x: from_list(FocusRect.from_dict, x), from_none], obj.get("faces"))
        return PurpleLarge(faces)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.faces is not None:
            result["faces"] = from_union([lambda x: from_list(lambda x: to_class(FocusRect, x), x), from_none], self.faces)
        return result


@dataclass
class PurpleFeatures:
    large: Optional[PurpleLarge] = None
    medium: Optional[PurpleLarge] = None
    small: Optional[PurpleLarge] = None
    orig: Optional[PurpleLarge] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PurpleFeatures':
        assert isinstance(obj, dict)
        large = from_union([PurpleLarge.from_dict, from_none], obj.get("large"))
        medium = from_union([PurpleLarge.from_dict, from_none], obj.get("medium"))
        small = from_union([PurpleLarge.from_dict, from_none], obj.get("small"))
        orig = from_union([PurpleLarge.from_dict, from_none], obj.get("orig"))
        return PurpleFeatures(large, medium, small, orig)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.large is not None:
            result["large"] = from_union([lambda x: to_class(PurpleLarge, x), from_none], self.large)
        if self.medium is not None:
            result["medium"] = from_union([lambda x: to_class(PurpleLarge, x), from_none], self.medium)
        if self.small is not None:
            result["small"] = from_union([lambda x: to_class(PurpleLarge, x), from_none], self.small)
        if self.orig is not None:
            result["orig"] = from_union([lambda x: to_class(PurpleLarge, x), from_none], self.orig)
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


class LargeResize(Enum):
    FIT = "fit"


@dataclass
class SizesLarge:
    h: Optional[int] = None
    w: Optional[int] = None
    resize: Optional[LargeResize] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SizesLarge':
        assert isinstance(obj, dict)
        h = from_union([from_int, from_none], obj.get("h"))
        w = from_union([from_int, from_none], obj.get("w"))
        resize = from_union([LargeResize, from_none], obj.get("resize"))
        return SizesLarge(h, w, resize)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.h is not None:
            result["h"] = from_union([from_int, from_none], self.h)
        if self.w is not None:
            result["w"] = from_union([from_int, from_none], self.w)
        if self.resize is not None:
            result["resize"] = from_union([lambda x: to_enum(LargeResize, x), from_none], self.resize)
        return result


class ThumbResize(Enum):
    CROP = "crop"


@dataclass
class Thumb:
    h: Optional[int] = None
    w: Optional[int] = None
    resize: Optional[ThumbResize] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Thumb':
        assert isinstance(obj, dict)
        h = from_union([from_int, from_none], obj.get("h"))
        w = from_union([from_int, from_none], obj.get("w"))
        resize = from_union([ThumbResize, from_none], obj.get("resize"))
        return Thumb(h, w, resize)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.h is not None:
            result["h"] = from_union([from_int, from_none], self.h)
        if self.w is not None:
            result["w"] = from_union([from_int, from_none], self.w)
        if self.resize is not None:
            result["resize"] = from_union([lambda x: to_enum(ThumbResize, x), from_none], self.resize)
        return result


@dataclass
class Sizes:
    large: Optional[SizesLarge] = None
    medium: Optional[SizesLarge] = None
    small: Optional[SizesLarge] = None
    thumb: Optional[Thumb] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Sizes':
        assert isinstance(obj, dict)
        large = from_union([SizesLarge.from_dict, from_none], obj.get("large"))
        medium = from_union([SizesLarge.from_dict, from_none], obj.get("medium"))
        small = from_union([SizesLarge.from_dict, from_none], obj.get("small"))
        thumb = from_union([Thumb.from_dict, from_none], obj.get("thumb"))
        return Sizes(large, medium, small, thumb)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.large is not None:
            result["large"] = from_union([lambda x: to_class(SizesLarge, x), from_none], self.large)
        if self.medium is not None:
            result["medium"] = from_union([lambda x: to_class(SizesLarge, x), from_none], self.medium)
        if self.small is not None:
            result["small"] = from_union([lambda x: to_class(SizesLarge, x), from_none], self.small)
        if self.thumb is not None:
            result["thumb"] = from_union([lambda x: to_class(Thumb, x), from_none], self.thumb)
        return result


class MediaType(Enum):
    ANIMATED_GIF = "animated_gif"
    PHOTO = "photo"


@dataclass
class PurpleMedia:
    display_url: Optional[str] = None
    expanded_url: Optional[str] = None
    id_str: Optional[str] = None
    indices: Optional[List[int]] = None
    media_url_https: Optional[str] = None
    type: Optional[MediaType] = None
    url: Optional[str] = None
    features: Optional[PurpleFeatures] = None
    sizes: Optional[Sizes] = None
    original_info: Optional[OriginalInfo] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PurpleMedia':
        assert isinstance(obj, dict)
        display_url = from_union([from_str, from_none], obj.get("display_url"))
        expanded_url = from_union([from_str, from_none], obj.get("expanded_url"))
        id_str = from_union([from_str, from_none], obj.get("id_str"))
        indices = from_union([lambda x: from_list(from_int, x), from_none], obj.get("indices"))
        media_url_https = from_union([from_str, from_none], obj.get("media_url_https"))
        type = from_union([MediaType, from_none], obj.get("type"))
        url = from_union([from_str, from_none], obj.get("url"))
        features = from_union([PurpleFeatures.from_dict, from_none], obj.get("features"))
        sizes = from_union([Sizes.from_dict, from_none], obj.get("sizes"))
        original_info = from_union([OriginalInfo.from_dict, from_none], obj.get("original_info"))
        return PurpleMedia(display_url, expanded_url, id_str, indices, media_url_https, type, url, features, sizes, original_info)

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
            result["features"] = from_union([lambda x: to_class(PurpleFeatures, x), from_none], self.features)
        if self.sizes is not None:
            result["sizes"] = from_union([lambda x: to_class(Sizes, x), from_none], self.sizes)
        if self.original_info is not None:
            result["original_info"] = from_union([lambda x: to_class(OriginalInfo, x), from_none], self.original_info)
        return result


@dataclass
class TentacledURL:
    display_url: Optional[str] = None
    expanded_url: Optional[str] = None
    url: Optional[str] = None
    indices: Optional[List[int]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TentacledURL':
        assert isinstance(obj, dict)
        display_url = from_union([from_str, from_none], obj.get("display_url"))
        expanded_url = from_union([from_str, from_none], obj.get("expanded_url"))
        url = from_union([from_str, from_none], obj.get("url"))
        indices = from_union([lambda x: from_list(from_int, x), from_none], obj.get("indices"))
        return TentacledURL(display_url, expanded_url, url, indices)

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
class PurpleUserMention:
    id_str: Optional[str] = None
    name: Optional[str] = None
    screen_name: Optional[str] = None
    indices: Optional[List[int]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PurpleUserMention':
        assert isinstance(obj, dict)
        id_str = from_union([from_str, from_none], obj.get("id_str"))
        name = from_union([from_str, from_none], obj.get("name"))
        screen_name = from_union([from_str, from_none], obj.get("screen_name"))
        indices = from_union([lambda x: from_list(from_int, x), from_none], obj.get("indices"))
        return PurpleUserMention(id_str, name, screen_name, indices)

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
    user_mentions: Optional[List[PurpleUserMention]] = None
    urls: Optional[List[TentacledURL]] = None
    hashtags: Optional[List[Hashtag]] = None
    symbols: Optional[List[Any]] = None
    media: Optional[List[PurpleMedia]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'FluffyEntities':
        assert isinstance(obj, dict)
        user_mentions = from_union([lambda x: from_list(PurpleUserMention.from_dict, x), from_none], obj.get("user_mentions"))
        urls = from_union([lambda x: from_list(TentacledURL.from_dict, x), from_none], obj.get("urls"))
        hashtags = from_union([lambda x: from_list(Hashtag.from_dict, x), from_none], obj.get("hashtags"))
        symbols = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("symbols"))
        media = from_union([lambda x: from_list(PurpleMedia.from_dict, x), from_none], obj.get("media"))
        return FluffyEntities(user_mentions, urls, hashtags, symbols, media)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.user_mentions is not None:
            result["user_mentions"] = from_union([lambda x: from_list(lambda x: to_class(PurpleUserMention, x), x), from_none], self.user_mentions)
        if self.urls is not None:
            result["urls"] = from_union([lambda x: from_list(lambda x: to_class(TentacledURL, x), x), from_none], self.urls)
        if self.hashtags is not None:
            result["hashtags"] = from_union([lambda x: from_list(lambda x: to_class(Hashtag, x), x), from_none], self.hashtags)
        if self.symbols is not None:
            result["symbols"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.symbols)
        if self.media is not None:
            result["media"] = from_union([lambda x: from_list(lambda x: to_class(PurpleMedia, x), x), from_none], self.media)
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
class Variant:
    bitrate: Optional[int] = None
    content_type: Optional[str] = None
    url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Variant':
        assert isinstance(obj, dict)
        bitrate = from_union([from_int, from_none], obj.get("bitrate"))
        content_type = from_union([from_str, from_none], obj.get("content_type"))
        url = from_union([from_str, from_none], obj.get("url"))
        return Variant(bitrate, content_type, url)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.bitrate is not None:
            result["bitrate"] = from_union([from_int, from_none], self.bitrate)
        if self.content_type is not None:
            result["content_type"] = from_union([from_str, from_none], self.content_type)
        if self.url is not None:
            result["url"] = from_union([from_str, from_none], self.url)
        return result


@dataclass
class VideoInfo:
    aspect_ratio: Optional[List[int]] = None
    variants: Optional[List[Variant]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'VideoInfo':
        assert isinstance(obj, dict)
        aspect_ratio = from_union([lambda x: from_list(from_int, x), from_none], obj.get("aspect_ratio"))
        variants = from_union([lambda x: from_list(Variant.from_dict, x), from_none], obj.get("variants"))
        return VideoInfo(aspect_ratio, variants)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.aspect_ratio is not None:
            result["aspect_ratio"] = from_union([lambda x: from_list(from_int, x), from_none], self.aspect_ratio)
        if self.variants is not None:
            result["variants"] = from_union([lambda x: from_list(lambda x: to_class(Variant, x), x), from_none], self.variants)
        return result


@dataclass
class FluffyMedia:
    display_url: Optional[str] = None
    expanded_url: Optional[str] = None
    id_str: Optional[str] = None
    indices: Optional[List[int]] = None
    media_key: Optional[str] = None
    media_url_https: Optional[str] = None
    type: Optional[MediaType] = None
    url: Optional[str] = None
    ext_media_availability: Optional[EXTMediaAvailability] = None
    features: Optional[PurpleFeatures] = None
    sizes: Optional[Sizes] = None
    original_info: Optional[OriginalInfo] = None
    video_info: Optional[VideoInfo] = None
    ext_alt_text: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'FluffyMedia':
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
        features = from_union([PurpleFeatures.from_dict, from_none], obj.get("features"))
        sizes = from_union([Sizes.from_dict, from_none], obj.get("sizes"))
        original_info = from_union([OriginalInfo.from_dict, from_none], obj.get("original_info"))
        video_info = from_union([VideoInfo.from_dict, from_none], obj.get("video_info"))
        ext_alt_text = from_union([from_str, from_none], obj.get("ext_alt_text"))
        return FluffyMedia(display_url, expanded_url, id_str, indices, media_key, media_url_https, type, url, ext_media_availability, features, sizes, original_info, video_info, ext_alt_text)

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
            result["features"] = from_union([lambda x: to_class(PurpleFeatures, x), from_none], self.features)
        if self.sizes is not None:
            result["sizes"] = from_union([lambda x: to_class(Sizes, x), from_none], self.sizes)
        if self.original_info is not None:
            result["original_info"] = from_union([lambda x: to_class(OriginalInfo, x), from_none], self.original_info)
        if self.video_info is not None:
            result["video_info"] = from_union([lambda x: to_class(VideoInfo, x), from_none], self.video_info)
        if self.ext_alt_text is not None:
            result["ext_alt_text"] = from_union([from_str, from_none], self.ext_alt_text)
        return result


@dataclass
class PurpleExtendedEntities:
    media: Optional[List[FluffyMedia]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PurpleExtendedEntities':
        assert isinstance(obj, dict)
        media = from_union([lambda x: from_list(FluffyMedia.from_dict, x), from_none], obj.get("media"))
        return PurpleExtendedEntities(media)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.media is not None:
            result["media"] = from_union([lambda x: from_list(lambda x: to_class(FluffyMedia, x), x), from_none], self.media)
        return result


class PurpleLang(Enum):
    EN = "en"
    FI = "fi"
    NO = "no"
    SV = "sv"


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
class StickyURL:
    urls: Optional[List[TentacledURL]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'StickyURL':
        assert isinstance(obj, dict)
        urls = from_union([lambda x: from_list(TentacledURL.from_dict, x), from_none], obj.get("urls"))
        return StickyURL(urls)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.urls is not None:
            result["urls"] = from_union([lambda x: from_list(lambda x: to_class(TentacledURL, x), x), from_none], self.urls)
        return result


@dataclass
class TentacledEntities:
    description: Optional[PurpleDescription] = None
    url: Optional[StickyURL] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TentacledEntities':
        assert isinstance(obj, dict)
        description = from_union([PurpleDescription.from_dict, from_none], obj.get("description"))
        url = from_union([StickyURL.from_dict, from_none], obj.get("url"))
        return TentacledEntities(description, url)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.description is not None:
            result["description"] = from_union([lambda x: to_class(PurpleDescription, x), from_none], self.description)
        if self.url is not None:
            result["url"] = from_union([lambda x: to_class(StickyURL, x), from_none], self.url)
        return result


@dataclass
class StickyLegacy:
    can_dm: Optional[bool] = None
    can_media_tag: Optional[bool] = None
    created_at: Optional[str] = None
    default_profile: Optional[bool] = None
    default_profile_image: Optional[bool] = None
    description: Optional[str] = None
    entities: Optional[TentacledEntities] = None
    fast_followers_count: Optional[int] = None
    favourites_count: Optional[int] = None
    followers_count: Optional[int] = None
    friends_count: Optional[int] = None
    has_custom_timelines: Optional[bool] = None
    is_translator: Optional[bool] = None
    listed_count: Optional[int] = None
    location: Optional[str] = None
    media_count: Optional[int] = None
    name: Optional[str] = None
    normal_followers_count: Optional[int] = None
    pinned_tweet_ids_str: Optional[List[Any]] = None
    possibly_sensitive: Optional[bool] = None
    profile_banner_url: Optional[str] = None
    profile_image_url_https: Optional[str] = None
    profile_interstitial_type: Optional[str] = None
    screen_name: Optional[str] = None
    statuses_count: Optional[int] = None
    translator_type: Optional[TranslatorType] = None
    url: Optional[str] = None
    verified: Optional[bool] = None
    want_retweets: Optional[bool] = None
    withheld_in_countries: Optional[List[Any]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'StickyLegacy':
        assert isinstance(obj, dict)
        can_dm = from_union([from_bool, from_none], obj.get("can_dm"))
        can_media_tag = from_union([from_bool, from_none], obj.get("can_media_tag"))
        created_at = from_union([from_str, from_none], obj.get("created_at"))
        default_profile = from_union([from_bool, from_none], obj.get("default_profile"))
        default_profile_image = from_union([from_bool, from_none], obj.get("default_profile_image"))
        description = from_union([from_str, from_none], obj.get("description"))
        entities = from_union([TentacledEntities.from_dict, from_none], obj.get("entities"))
        fast_followers_count = from_union([from_int, from_none], obj.get("fast_followers_count"))
        favourites_count = from_union([from_int, from_none], obj.get("favourites_count"))
        followers_count = from_union([from_int, from_none], obj.get("followers_count"))
        friends_count = from_union([from_int, from_none], obj.get("friends_count"))
        has_custom_timelines = from_union([from_bool, from_none], obj.get("has_custom_timelines"))
        is_translator = from_union([from_bool, from_none], obj.get("is_translator"))
        listed_count = from_union([from_int, from_none], obj.get("listed_count"))
        location = from_union([from_str, from_none], obj.get("location"))
        media_count = from_union([from_int, from_none], obj.get("media_count"))
        name = from_union([from_str, from_none], obj.get("name"))
        normal_followers_count = from_union([from_int, from_none], obj.get("normal_followers_count"))
        pinned_tweet_ids_str = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("pinned_tweet_ids_str"))
        possibly_sensitive = from_union([from_bool, from_none], obj.get("possibly_sensitive"))
        profile_banner_url = from_union([from_str, from_none], obj.get("profile_banner_url"))
        profile_image_url_https = from_union([from_str, from_none], obj.get("profile_image_url_https"))
        profile_interstitial_type = from_union([from_str, from_none], obj.get("profile_interstitial_type"))
        screen_name = from_union([from_str, from_none], obj.get("screen_name"))
        statuses_count = from_union([from_int, from_none], obj.get("statuses_count"))
        translator_type = from_union([TranslatorType, from_none], obj.get("translator_type"))
        url = from_union([from_str, from_none], obj.get("url"))
        verified = from_union([from_bool, from_none], obj.get("verified"))
        want_retweets = from_union([from_bool, from_none], obj.get("want_retweets"))
        withheld_in_countries = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("withheld_in_countries"))
        return StickyLegacy(can_dm, can_media_tag, created_at, default_profile, default_profile_image, description, entities, fast_followers_count, favourites_count, followers_count, friends_count, has_custom_timelines, is_translator, listed_count, location, media_count, name, normal_followers_count, pinned_tweet_ids_str, possibly_sensitive, profile_banner_url, profile_image_url_https, profile_interstitial_type, screen_name, statuses_count, translator_type, url, verified, want_retweets, withheld_in_countries)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.can_dm is not None:
            result["can_dm"] = from_union([from_bool, from_none], self.can_dm)
        if self.can_media_tag is not None:
            result["can_media_tag"] = from_union([from_bool, from_none], self.can_media_tag)
        if self.created_at is not None:
            result["created_at"] = from_union([from_str, from_none], self.created_at)
        if self.default_profile is not None:
            result["default_profile"] = from_union([from_bool, from_none], self.default_profile)
        if self.default_profile_image is not None:
            result["default_profile_image"] = from_union([from_bool, from_none], self.default_profile_image)
        if self.description is not None:
            result["description"] = from_union([from_str, from_none], self.description)
        if self.entities is not None:
            result["entities"] = from_union([lambda x: to_class(TentacledEntities, x), from_none], self.entities)
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
            result["location"] = from_union([from_str, from_none], self.location)
        if self.media_count is not None:
            result["media_count"] = from_union([from_int, from_none], self.media_count)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.normal_followers_count is not None:
            result["normal_followers_count"] = from_union([from_int, from_none], self.normal_followers_count)
        if self.pinned_tweet_ids_str is not None:
            result["pinned_tweet_ids_str"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.pinned_tweet_ids_str)
        if self.possibly_sensitive is not None:
            result["possibly_sensitive"] = from_union([from_bool, from_none], self.possibly_sensitive)
        if self.profile_banner_url is not None:
            result["profile_banner_url"] = from_union([from_str, from_none], self.profile_banner_url)
        if self.profile_image_url_https is not None:
            result["profile_image_url_https"] = from_union([from_str, from_none], self.profile_image_url_https)
        if self.profile_interstitial_type is not None:
            result["profile_interstitial_type"] = from_union([from_str, from_none], self.profile_interstitial_type)
        if self.screen_name is not None:
            result["screen_name"] = from_union([from_str, from_none], self.screen_name)
        if self.statuses_count is not None:
            result["statuses_count"] = from_union([from_int, from_none], self.statuses_count)
        if self.translator_type is not None:
            result["translator_type"] = from_union([lambda x: to_enum(TranslatorType, x), from_none], self.translator_type)
        if self.url is not None:
            result["url"] = from_union([from_str, from_none], self.url)
        if self.verified is not None:
            result["verified"] = from_union([from_bool, from_none], self.verified)
        if self.want_retweets is not None:
            result["want_retweets"] = from_union([from_bool, from_none], self.want_retweets)
        if self.withheld_in_countries is not None:
            result["withheld_in_countries"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.withheld_in_countries)
        return result


@dataclass
class TentacledResult:
    typename: Optional[UserDisplayTypeEnum] = None
    id: Optional[str] = None
    rest_id: Optional[str] = None
    affiliates_highlighted_label: Optional[AffiliatesHighlightedLabel] = None
    has_graduated_access: Optional[bool] = None
    is_blue_verified: Optional[bool] = None
    profile_image_shape: Optional[ProfileImageShape] = None
    legacy: Optional[StickyLegacy] = None
    smart_blocked_by: Optional[bool] = None
    smart_blocking: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TentacledResult':
        assert isinstance(obj, dict)
        typename = from_union([UserDisplayTypeEnum, from_none], obj.get("__typename"))
        id = from_union([from_str, from_none], obj.get("id"))
        rest_id = from_union([from_str, from_none], obj.get("rest_id"))
        affiliates_highlighted_label = from_union([AffiliatesHighlightedLabel.from_dict, from_none], obj.get("affiliates_highlighted_label"))
        has_graduated_access = from_union([from_bool, from_none], obj.get("has_graduated_access"))
        is_blue_verified = from_union([from_bool, from_none], obj.get("is_blue_verified"))
        profile_image_shape = from_union([ProfileImageShape, from_none], obj.get("profile_image_shape"))
        legacy = from_union([StickyLegacy.from_dict, from_none], obj.get("legacy"))
        smart_blocked_by = from_union([from_bool, from_none], obj.get("smart_blocked_by"))
        smart_blocking = from_union([from_bool, from_none], obj.get("smart_blocking"))
        return TentacledResult(typename, id, rest_id, affiliates_highlighted_label, has_graduated_access, is_blue_verified, profile_image_shape, legacy, smart_blocked_by, smart_blocking)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.typename is not None:
            result["__typename"] = from_union([lambda x: to_enum(UserDisplayTypeEnum, x), from_none], self.typename)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.rest_id is not None:
            result["rest_id"] = from_union([from_str, from_none], self.rest_id)
        if self.affiliates_highlighted_label is not None:
            result["affiliates_highlighted_label"] = from_union([lambda x: to_class(AffiliatesHighlightedLabel, x), from_none], self.affiliates_highlighted_label)
        if self.has_graduated_access is not None:
            result["has_graduated_access"] = from_union([from_bool, from_none], self.has_graduated_access)
        if self.is_blue_verified is not None:
            result["is_blue_verified"] = from_union([from_bool, from_none], self.is_blue_verified)
        if self.profile_image_shape is not None:
            result["profile_image_shape"] = from_union([lambda x: to_enum(ProfileImageShape, x), from_none], self.profile_image_shape)
        if self.legacy is not None:
            result["legacy"] = from_union([lambda x: to_class(StickyLegacy, x), from_none], self.legacy)
        if self.smart_blocked_by is not None:
            result["smart_blocked_by"] = from_union([from_bool, from_none], self.smart_blocked_by)
        if self.smart_blocking is not None:
            result["smart_blocking"] = from_union([from_bool, from_none], self.smart_blocking)
        return result


@dataclass
class FluffyUserResults:
    result: Optional[TentacledResult] = None

    @staticmethod
    def from_dict(obj: Any) -> 'FluffyUserResults':
        assert isinstance(obj, dict)
        result = from_union([TentacledResult.from_dict, from_none], obj.get("result"))
        return FluffyUserResults(result)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.result is not None:
            result["result"] = from_union([lambda x: to_class(TentacledResult, x), from_none], self.result)
        return result


@dataclass
class FluffyCore:
    user_results: Optional[FluffyUserResults] = None

    @staticmethod
    def from_dict(obj: Any) -> 'FluffyCore':
        assert isinstance(obj, dict)
        user_results = from_union([FluffyUserResults.from_dict, from_none], obj.get("user_results"))
        return FluffyCore(user_results)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.user_results is not None:
            result["user_results"] = from_union([lambda x: to_class(FluffyUserResults, x), from_none], self.user_results)
        return result


class Element(Enum):
    TWEET = "tweet"
    USER = "user"


@dataclass
class Tag:
    user_id: Optional[str] = None
    name: Optional[str] = None
    screen_name: Optional[str] = None
    type: Optional[Element] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Tag':
        assert isinstance(obj, dict)
        user_id = from_union([from_str, from_none], obj.get("user_id"))
        name = from_union([from_str, from_none], obj.get("name"))
        screen_name = from_union([from_str, from_none], obj.get("screen_name"))
        type = from_union([Element, from_none], obj.get("type"))
        return Tag(user_id, name, screen_name, type)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.user_id is not None:
            result["user_id"] = from_union([from_str, from_none], self.user_id)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.screen_name is not None:
            result["screen_name"] = from_union([from_str, from_none], self.screen_name)
        if self.type is not None:
            result["type"] = from_union([lambda x: to_enum(Element, x), from_none], self.type)
        return result


@dataclass
class All:
    tags: Optional[List[Tag]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'All':
        assert isinstance(obj, dict)
        tags = from_union([lambda x: from_list(Tag.from_dict, x), from_none], obj.get("tags"))
        return All(tags)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.tags is not None:
            result["tags"] = from_union([lambda x: from_list(lambda x: to_class(Tag, x), x), from_none], self.tags)
        return result


@dataclass
class FluffyLarge:
    faces: Optional[List[Any]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'FluffyLarge':
        assert isinstance(obj, dict)
        faces = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("faces"))
        return FluffyLarge(faces)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.faces is not None:
            result["faces"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.faces)
        return result


@dataclass
class FluffyFeatures:
    all: Optional[All] = None
    large: Optional[FluffyLarge] = None
    medium: Optional[FluffyLarge] = None
    small: Optional[FluffyLarge] = None
    orig: Optional[FluffyLarge] = None

    @staticmethod
    def from_dict(obj: Any) -> 'FluffyFeatures':
        assert isinstance(obj, dict)
        all = from_union([All.from_dict, from_none], obj.get("all"))
        large = from_union([FluffyLarge.from_dict, from_none], obj.get("large"))
        medium = from_union([FluffyLarge.from_dict, from_none], obj.get("medium"))
        small = from_union([FluffyLarge.from_dict, from_none], obj.get("small"))
        orig = from_union([FluffyLarge.from_dict, from_none], obj.get("orig"))
        return FluffyFeatures(all, large, medium, small, orig)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.all is not None:
            result["all"] = from_union([lambda x: to_class(All, x), from_none], self.all)
        if self.large is not None:
            result["large"] = from_union([lambda x: to_class(FluffyLarge, x), from_none], self.large)
        if self.medium is not None:
            result["medium"] = from_union([lambda x: to_class(FluffyLarge, x), from_none], self.medium)
        if self.small is not None:
            result["small"] = from_union([lambda x: to_class(FluffyLarge, x), from_none], self.small)
        if self.orig is not None:
            result["orig"] = from_union([lambda x: to_class(FluffyLarge, x), from_none], self.orig)
        return result


@dataclass
class TentacledMedia:
    display_url: Optional[str] = None
    expanded_url: Optional[str] = None
    id_str: Optional[str] = None
    indices: Optional[List[int]] = None
    media_url_https: Optional[str] = None
    type: Optional[MediaType] = None
    url: Optional[str] = None
    features: Optional[FluffyFeatures] = None
    sizes: Optional[Sizes] = None
    original_info: Optional[OriginalInfo] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TentacledMedia':
        assert isinstance(obj, dict)
        display_url = from_union([from_str, from_none], obj.get("display_url"))
        expanded_url = from_union([from_str, from_none], obj.get("expanded_url"))
        id_str = from_union([from_str, from_none], obj.get("id_str"))
        indices = from_union([lambda x: from_list(from_int, x), from_none], obj.get("indices"))
        media_url_https = from_union([from_str, from_none], obj.get("media_url_https"))
        type = from_union([MediaType, from_none], obj.get("type"))
        url = from_union([from_str, from_none], obj.get("url"))
        features = from_union([FluffyFeatures.from_dict, from_none], obj.get("features"))
        sizes = from_union([Sizes.from_dict, from_none], obj.get("sizes"))
        original_info = from_union([OriginalInfo.from_dict, from_none], obj.get("original_info"))
        return TentacledMedia(display_url, expanded_url, id_str, indices, media_url_https, type, url, features, sizes, original_info)

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
            result["features"] = from_union([lambda x: to_class(FluffyFeatures, x), from_none], self.features)
        if self.sizes is not None:
            result["sizes"] = from_union([lambda x: to_class(Sizes, x), from_none], self.sizes)
        if self.original_info is not None:
            result["original_info"] = from_union([lambda x: to_class(OriginalInfo, x), from_none], self.original_info)
        return result


@dataclass
class FluffyUserMention:
    id_str: Optional[int] = None
    name: Optional[str] = None
    screen_name: Optional[str] = None
    indices: Optional[List[int]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'FluffyUserMention':
        assert isinstance(obj, dict)
        id_str = from_union([from_none, lambda x: int(from_str(x))], obj.get("id_str"))
        name = from_union([from_str, from_none], obj.get("name"))
        screen_name = from_union([from_str, from_none], obj.get("screen_name"))
        indices = from_union([lambda x: from_list(from_int, x), from_none], obj.get("indices"))
        return FluffyUserMention(id_str, name, screen_name, indices)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.id_str is not None:
            result["id_str"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.id_str)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.screen_name is not None:
            result["screen_name"] = from_union([from_str, from_none], self.screen_name)
        if self.indices is not None:
            result["indices"] = from_union([lambda x: from_list(from_int, x), from_none], self.indices)
        return result


@dataclass
class StickyEntities:
    user_mentions: Optional[List[FluffyUserMention]] = None
    urls: Optional[List[Any]] = None
    hashtags: Optional[List[Hashtag]] = None
    symbols: Optional[List[Any]] = None
    media: Optional[List[TentacledMedia]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'StickyEntities':
        assert isinstance(obj, dict)
        user_mentions = from_union([lambda x: from_list(FluffyUserMention.from_dict, x), from_none], obj.get("user_mentions"))
        urls = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("urls"))
        hashtags = from_union([lambda x: from_list(Hashtag.from_dict, x), from_none], obj.get("hashtags"))
        symbols = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("symbols"))
        media = from_union([lambda x: from_list(TentacledMedia.from_dict, x), from_none], obj.get("media"))
        return StickyEntities(user_mentions, urls, hashtags, symbols, media)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.user_mentions is not None:
            result["user_mentions"] = from_union([lambda x: from_list(lambda x: to_class(FluffyUserMention, x), x), from_none], self.user_mentions)
        if self.urls is not None:
            result["urls"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.urls)
        if self.hashtags is not None:
            result["hashtags"] = from_union([lambda x: from_list(lambda x: to_class(Hashtag, x), x), from_none], self.hashtags)
        if self.symbols is not None:
            result["symbols"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.symbols)
        if self.media is not None:
            result["media"] = from_union([lambda x: from_list(lambda x: to_class(TentacledMedia, x), x), from_none], self.media)
        return result


@dataclass
class StickyMedia:
    display_url: Optional[str] = None
    expanded_url: Optional[str] = None
    id_str: Optional[str] = None
    indices: Optional[List[int]] = None
    media_key: Optional[str] = None
    media_url_https: Optional[str] = None
    type: Optional[MediaType] = None
    url: Optional[str] = None
    ext_media_availability: Optional[EXTMediaAvailability] = None
    features: Optional[FluffyFeatures] = None
    sizes: Optional[Sizes] = None
    original_info: Optional[OriginalInfo] = None

    @staticmethod
    def from_dict(obj: Any) -> 'StickyMedia':
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
        features = from_union([FluffyFeatures.from_dict, from_none], obj.get("features"))
        sizes = from_union([Sizes.from_dict, from_none], obj.get("sizes"))
        original_info = from_union([OriginalInfo.from_dict, from_none], obj.get("original_info"))
        return StickyMedia(display_url, expanded_url, id_str, indices, media_key, media_url_https, type, url, ext_media_availability, features, sizes, original_info)

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
            result["features"] = from_union([lambda x: to_class(FluffyFeatures, x), from_none], self.features)
        if self.sizes is not None:
            result["sizes"] = from_union([lambda x: to_class(Sizes, x), from_none], self.sizes)
        if self.original_info is not None:
            result["original_info"] = from_union([lambda x: to_class(OriginalInfo, x), from_none], self.original_info)
        return result


@dataclass
class FluffyExtendedEntities:
    media: Optional[List[StickyMedia]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'FluffyExtendedEntities':
        assert isinstance(obj, dict)
        media = from_union([lambda x: from_list(StickyMedia.from_dict, x), from_none], obj.get("media"))
        return FluffyExtendedEntities(media)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.media is not None:
            result["media"] = from_union([lambda x: from_list(lambda x: to_class(StickyMedia, x), x), from_none], self.media)
        return result


@dataclass
class IndigoLegacy:
    bookmark_count: Optional[int] = None
    bookmarked: Optional[bool] = None
    created_at: Optional[str] = None
    conversation_id_str: Optional[str] = None
    display_text_range: Optional[List[int]] = None
    entities: Optional[StickyEntities] = None
    favorite_count: Optional[int] = None
    favorited: Optional[bool] = None
    full_text: Optional[str] = None
    is_quote_status: Optional[bool] = None
    lang: Optional[PurpleLang] = None
    quote_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None
    retweeted: Optional[bool] = None
    user_id_str: Optional[str] = None
    id_str: Optional[str] = None
    extended_entities: Optional[FluffyExtendedEntities] = None
    possibly_sensitive: Optional[bool] = None
    possibly_sensitive_editable: Optional[bool] = None
    quoted_status_id_str: Optional[str] = None
    quoted_status_permalink: Optional[QuotedStatusPermalink] = None

    @staticmethod
    def from_dict(obj: Any) -> 'IndigoLegacy':
        assert isinstance(obj, dict)
        bookmark_count = from_union([from_int, from_none], obj.get("bookmark_count"))
        bookmarked = from_union([from_bool, from_none], obj.get("bookmarked"))
        created_at = from_union([from_str, from_none], obj.get("created_at"))
        conversation_id_str = from_union([from_str, from_none], obj.get("conversation_id_str"))
        display_text_range = from_union([lambda x: from_list(from_int, x), from_none], obj.get("display_text_range"))
        entities = from_union([StickyEntities.from_dict, from_none], obj.get("entities"))
        favorite_count = from_union([from_int, from_none], obj.get("favorite_count"))
        favorited = from_union([from_bool, from_none], obj.get("favorited"))
        full_text = from_union([from_str, from_none], obj.get("full_text"))
        is_quote_status = from_union([from_bool, from_none], obj.get("is_quote_status"))
        lang = from_union([PurpleLang, from_none], obj.get("lang"))
        quote_count = from_union([from_int, from_none], obj.get("quote_count"))
        reply_count = from_union([from_int, from_none], obj.get("reply_count"))
        retweet_count = from_union([from_int, from_none], obj.get("retweet_count"))
        retweeted = from_union([from_bool, from_none], obj.get("retweeted"))
        user_id_str = from_union([from_str, from_none], obj.get("user_id_str"))
        id_str = from_union([from_str, from_none], obj.get("id_str"))
        extended_entities = from_union([FluffyExtendedEntities.from_dict, from_none], obj.get("extended_entities"))
        possibly_sensitive = from_union([from_bool, from_none], obj.get("possibly_sensitive"))
        possibly_sensitive_editable = from_union([from_bool, from_none], obj.get("possibly_sensitive_editable"))
        quoted_status_id_str = from_union([from_str, from_none], obj.get("quoted_status_id_str"))
        quoted_status_permalink = from_union([QuotedStatusPermalink.from_dict, from_none], obj.get("quoted_status_permalink"))
        return IndigoLegacy(bookmark_count, bookmarked, created_at, conversation_id_str, display_text_range, entities, favorite_count, favorited, full_text, is_quote_status, lang, quote_count, reply_count, retweet_count, retweeted, user_id_str, id_str, extended_entities, possibly_sensitive, possibly_sensitive_editable, quoted_status_id_str, quoted_status_permalink)

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
            result["entities"] = from_union([lambda x: to_class(StickyEntities, x), from_none], self.entities)
        if self.favorite_count is not None:
            result["favorite_count"] = from_union([from_int, from_none], self.favorite_count)
        if self.favorited is not None:
            result["favorited"] = from_union([from_bool, from_none], self.favorited)
        if self.full_text is not None:
            result["full_text"] = from_union([from_str, from_none], self.full_text)
        if self.is_quote_status is not None:
            result["is_quote_status"] = from_union([from_bool, from_none], self.is_quote_status)
        if self.lang is not None:
            result["lang"] = from_union([lambda x: to_enum(PurpleLang, x), from_none], self.lang)
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
        if self.extended_entities is not None:
            result["extended_entities"] = from_union([lambda x: to_class(FluffyExtendedEntities, x), from_none], self.extended_entities)
        if self.possibly_sensitive is not None:
            result["possibly_sensitive"] = from_union([from_bool, from_none], self.possibly_sensitive)
        if self.possibly_sensitive_editable is not None:
            result["possibly_sensitive_editable"] = from_union([from_bool, from_none], self.possibly_sensitive_editable)
        if self.quoted_status_id_str is not None:
            result["quoted_status_id_str"] = from_union([from_str, from_none], self.quoted_status_id_str)
        if self.quoted_status_permalink is not None:
            result["quoted_status_permalink"] = from_union([lambda x: to_class(QuotedStatusPermalink, x), from_none], self.quoted_status_permalink)
        return result


@dataclass
class IndecentLegacy:
    can_dm: Optional[bool] = None
    can_media_tag: Optional[bool] = None
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
    pinned_tweet_ids_str: Optional[List[Any]] = None
    possibly_sensitive: Optional[bool] = None
    profile_banner_url: Optional[str] = None
    profile_image_url_https: Optional[str] = None
    profile_interstitial_type: Optional[str] = None
    screen_name: Optional[Name] = None
    statuses_count: Optional[int] = None
    translator_type: Optional[TranslatorType] = None
    url: Optional[str] = None
    verified: Optional[bool] = None
    want_retweets: Optional[bool] = None
    withheld_in_countries: Optional[List[Any]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'IndecentLegacy':
        assert isinstance(obj, dict)
        can_dm = from_union([from_bool, from_none], obj.get("can_dm"))
        can_media_tag = from_union([from_bool, from_none], obj.get("can_media_tag"))
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
        pinned_tweet_ids_str = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("pinned_tweet_ids_str"))
        possibly_sensitive = from_union([from_bool, from_none], obj.get("possibly_sensitive"))
        profile_banner_url = from_union([from_str, from_none], obj.get("profile_banner_url"))
        profile_image_url_https = from_union([from_str, from_none], obj.get("profile_image_url_https"))
        profile_interstitial_type = from_union([from_str, from_none], obj.get("profile_interstitial_type"))
        screen_name = from_union([Name, from_none], obj.get("screen_name"))
        statuses_count = from_union([from_int, from_none], obj.get("statuses_count"))
        translator_type = from_union([TranslatorType, from_none], obj.get("translator_type"))
        url = from_union([from_str, from_none], obj.get("url"))
        verified = from_union([from_bool, from_none], obj.get("verified"))
        want_retweets = from_union([from_bool, from_none], obj.get("want_retweets"))
        withheld_in_countries = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("withheld_in_countries"))
        return IndecentLegacy(can_dm, can_media_tag, created_at, default_profile, default_profile_image, description, entities, fast_followers_count, favourites_count, followers_count, friends_count, has_custom_timelines, is_translator, listed_count, location, media_count, name, normal_followers_count, pinned_tweet_ids_str, possibly_sensitive, profile_banner_url, profile_image_url_https, profile_interstitial_type, screen_name, statuses_count, translator_type, url, verified, want_retweets, withheld_in_countries)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.can_dm is not None:
            result["can_dm"] = from_union([from_bool, from_none], self.can_dm)
        if self.can_media_tag is not None:
            result["can_media_tag"] = from_union([from_bool, from_none], self.can_media_tag)
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
            result["pinned_tweet_ids_str"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.pinned_tweet_ids_str)
        if self.possibly_sensitive is not None:
            result["possibly_sensitive"] = from_union([from_bool, from_none], self.possibly_sensitive)
        if self.profile_banner_url is not None:
            result["profile_banner_url"] = from_union([from_str, from_none], self.profile_banner_url)
        if self.profile_image_url_https is not None:
            result["profile_image_url_https"] = from_union([from_str, from_none], self.profile_image_url_https)
        if self.profile_interstitial_type is not None:
            result["profile_interstitial_type"] = from_union([from_str, from_none], self.profile_interstitial_type)
        if self.screen_name is not None:
            result["screen_name"] = from_union([lambda x: to_enum(Name, x), from_none], self.screen_name)
        if self.statuses_count is not None:
            result["statuses_count"] = from_union([from_int, from_none], self.statuses_count)
        if self.translator_type is not None:
            result["translator_type"] = from_union([lambda x: to_enum(TranslatorType, x), from_none], self.translator_type)
        if self.url is not None:
            result["url"] = from_union([from_str, from_none], self.url)
        if self.verified is not None:
            result["verified"] = from_union([from_bool, from_none], self.verified)
        if self.want_retweets is not None:
            result["want_retweets"] = from_union([from_bool, from_none], self.want_retweets)
        if self.withheld_in_countries is not None:
            result["withheld_in_countries"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.withheld_in_countries)
        return result


@dataclass
class IndigoResult:
    rest_id: Optional[int] = None
    typename: Optional[UserDisplayTypeEnum] = None
    id: Optional[ID] = None
    affiliates_highlighted_label: Optional[AffiliatesHighlightedLabel] = None
    has_graduated_access: Optional[bool] = None
    is_blue_verified: Optional[bool] = None
    profile_image_shape: Optional[ProfileImageShape] = None
    legacy: Optional[IndecentLegacy] = None
    smart_blocked_by: Optional[bool] = None
    smart_blocking: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'IndigoResult':
        assert isinstance(obj, dict)
        rest_id = from_union([from_none, lambda x: int(from_str(x))], obj.get("rest_id"))
        typename = from_union([UserDisplayTypeEnum, from_none], obj.get("__typename"))
        id = from_union([ID, from_none], obj.get("id"))
        affiliates_highlighted_label = from_union([AffiliatesHighlightedLabel.from_dict, from_none], obj.get("affiliates_highlighted_label"))
        has_graduated_access = from_union([from_bool, from_none], obj.get("has_graduated_access"))
        is_blue_verified = from_union([from_bool, from_none], obj.get("is_blue_verified"))
        profile_image_shape = from_union([ProfileImageShape, from_none], obj.get("profile_image_shape"))
        legacy = from_union([IndecentLegacy.from_dict, from_none], obj.get("legacy"))
        smart_blocked_by = from_union([from_bool, from_none], obj.get("smart_blocked_by"))
        smart_blocking = from_union([from_bool, from_none], obj.get("smart_blocking"))
        return IndigoResult(rest_id, typename, id, affiliates_highlighted_label, has_graduated_access, is_blue_verified, profile_image_shape, legacy, smart_blocked_by, smart_blocking)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.rest_id is not None:
            result["rest_id"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.rest_id)
        if self.typename is not None:
            result["__typename"] = from_union([lambda x: to_enum(UserDisplayTypeEnum, x), from_none], self.typename)
        if self.id is not None:
            result["id"] = from_union([lambda x: to_enum(ID, x), from_none], self.id)
        if self.affiliates_highlighted_label is not None:
            result["affiliates_highlighted_label"] = from_union([lambda x: to_class(AffiliatesHighlightedLabel, x), from_none], self.affiliates_highlighted_label)
        if self.has_graduated_access is not None:
            result["has_graduated_access"] = from_union([from_bool, from_none], self.has_graduated_access)
        if self.is_blue_verified is not None:
            result["is_blue_verified"] = from_union([from_bool, from_none], self.is_blue_verified)
        if self.profile_image_shape is not None:
            result["profile_image_shape"] = from_union([lambda x: to_enum(ProfileImageShape, x), from_none], self.profile_image_shape)
        if self.legacy is not None:
            result["legacy"] = from_union([lambda x: to_class(IndecentLegacy, x), from_none], self.legacy)
        if self.smart_blocked_by is not None:
            result["smart_blocked_by"] = from_union([from_bool, from_none], self.smart_blocked_by)
        if self.smart_blocking is not None:
            result["smart_blocking"] = from_union([from_bool, from_none], self.smart_blocking)
        return result


@dataclass
class TentacledUserResults:
    result: Optional[IndigoResult] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TentacledUserResults':
        assert isinstance(obj, dict)
        result = from_union([IndigoResult.from_dict, from_none], obj.get("result"))
        return TentacledUserResults(result)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.result is not None:
            result["result"] = from_union([lambda x: to_class(IndigoResult, x), from_none], self.result)
        return result


@dataclass
class TentacledCore:
    user_results: Optional[TentacledUserResults] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TentacledCore':
        assert isinstance(obj, dict)
        user_results = from_union([TentacledUserResults.from_dict, from_none], obj.get("user_results"))
        return TentacledCore(user_results)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.user_results is not None:
            result["user_results"] = from_union([lambda x: to_class(TentacledUserResults, x), from_none], self.user_results)
        return result


@dataclass
class IndigoMedia:
    display_url: Optional[str] = None
    expanded_url: Optional[str] = None
    id_str: Optional[str] = None
    indices: Optional[List[int]] = None
    media_url_https: Optional[str] = None
    type: Optional[MediaType] = None
    url: Optional[str] = None
    features: Optional[PurpleFeatures] = None
    sizes: Optional[Sizes] = None
    original_info: Optional[OriginalInfo] = None

    @staticmethod
    def from_dict(obj: Any) -> 'IndigoMedia':
        assert isinstance(obj, dict)
        display_url = from_union([from_str, from_none], obj.get("display_url"))
        expanded_url = from_union([from_str, from_none], obj.get("expanded_url"))
        id_str = from_union([from_str, from_none], obj.get("id_str"))
        indices = from_union([lambda x: from_list(from_int, x), from_none], obj.get("indices"))
        media_url_https = from_union([from_str, from_none], obj.get("media_url_https"))
        type = from_union([MediaType, from_none], obj.get("type"))
        url = from_union([from_str, from_none], obj.get("url"))
        features = from_union([PurpleFeatures.from_dict, from_none], obj.get("features"))
        sizes = from_union([Sizes.from_dict, from_none], obj.get("sizes"))
        original_info = from_union([OriginalInfo.from_dict, from_none], obj.get("original_info"))
        return IndigoMedia(display_url, expanded_url, id_str, indices, media_url_https, type, url, features, sizes, original_info)

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
            result["features"] = from_union([lambda x: to_class(PurpleFeatures, x), from_none], self.features)
        if self.sizes is not None:
            result["sizes"] = from_union([lambda x: to_class(Sizes, x), from_none], self.sizes)
        if self.original_info is not None:
            result["original_info"] = from_union([lambda x: to_class(OriginalInfo, x), from_none], self.original_info)
        return result


@dataclass
class IndigoEntities:
    media: Optional[List[IndigoMedia]] = None
    user_mentions: Optional[List[Any]] = None
    urls: Optional[List[Any]] = None
    hashtags: Optional[List[Any]] = None
    symbols: Optional[List[Any]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'IndigoEntities':
        assert isinstance(obj, dict)
        media = from_union([lambda x: from_list(IndigoMedia.from_dict, x), from_none], obj.get("media"))
        user_mentions = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("user_mentions"))
        urls = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("urls"))
        hashtags = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("hashtags"))
        symbols = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("symbols"))
        return IndigoEntities(media, user_mentions, urls, hashtags, symbols)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.media is not None:
            result["media"] = from_union([lambda x: from_list(lambda x: to_class(IndigoMedia, x), x), from_none], self.media)
        if self.user_mentions is not None:
            result["user_mentions"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.user_mentions)
        if self.urls is not None:
            result["urls"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.urls)
        if self.hashtags is not None:
            result["hashtags"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.hashtags)
        if self.symbols is not None:
            result["symbols"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.symbols)
        return result


@dataclass
class IndecentMedia:
    display_url: Optional[str] = None
    expanded_url: Optional[str] = None
    id_str: Optional[str] = None
    indices: Optional[List[int]] = None
    media_key: Optional[str] = None
    media_url_https: Optional[str] = None
    type: Optional[MediaType] = None
    url: Optional[str] = None
    ext_media_availability: Optional[EXTMediaAvailability] = None
    features: Optional[PurpleFeatures] = None
    sizes: Optional[Sizes] = None
    original_info: Optional[OriginalInfo] = None

    @staticmethod
    def from_dict(obj: Any) -> 'IndecentMedia':
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
        features = from_union([PurpleFeatures.from_dict, from_none], obj.get("features"))
        sizes = from_union([Sizes.from_dict, from_none], obj.get("sizes"))
        original_info = from_union([OriginalInfo.from_dict, from_none], obj.get("original_info"))
        return IndecentMedia(display_url, expanded_url, id_str, indices, media_key, media_url_https, type, url, ext_media_availability, features, sizes, original_info)

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
            result["features"] = from_union([lambda x: to_class(PurpleFeatures, x), from_none], self.features)
        if self.sizes is not None:
            result["sizes"] = from_union([lambda x: to_class(Sizes, x), from_none], self.sizes)
        if self.original_info is not None:
            result["original_info"] = from_union([lambda x: to_class(OriginalInfo, x), from_none], self.original_info)
        return result


@dataclass
class TentacledExtendedEntities:
    media: Optional[List[IndecentMedia]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TentacledExtendedEntities':
        assert isinstance(obj, dict)
        media = from_union([lambda x: from_list(IndecentMedia.from_dict, x), from_none], obj.get("media"))
        return TentacledExtendedEntities(media)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.media is not None:
            result["media"] = from_union([lambda x: from_list(lambda x: to_class(IndecentMedia, x), x), from_none], self.media)
        return result


@dataclass
class HilariousLegacy:
    user_id_str: Optional[int] = None
    bookmark_count: Optional[int] = None
    bookmarked: Optional[bool] = None
    created_at: Optional[str] = None
    conversation_id_str: Optional[str] = None
    display_text_range: Optional[List[int]] = None
    entities: Optional[IndigoEntities] = None
    extended_entities: Optional[TentacledExtendedEntities] = None
    favorite_count: Optional[int] = None
    favorited: Optional[bool] = None
    full_text: Optional[str] = None
    is_quote_status: Optional[bool] = None
    lang: Optional[PurpleLang] = None
    possibly_sensitive: Optional[bool] = None
    possibly_sensitive_editable: Optional[bool] = None
    quote_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None
    retweeted: Optional[bool] = None
    id_str: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'HilariousLegacy':
        assert isinstance(obj, dict)
        user_id_str = from_union([from_none, lambda x: int(from_str(x))], obj.get("user_id_str"))
        bookmark_count = from_union([from_int, from_none], obj.get("bookmark_count"))
        bookmarked = from_union([from_bool, from_none], obj.get("bookmarked"))
        created_at = from_union([from_str, from_none], obj.get("created_at"))
        conversation_id_str = from_union([from_str, from_none], obj.get("conversation_id_str"))
        display_text_range = from_union([lambda x: from_list(from_int, x), from_none], obj.get("display_text_range"))
        entities = from_union([IndigoEntities.from_dict, from_none], obj.get("entities"))
        extended_entities = from_union([TentacledExtendedEntities.from_dict, from_none], obj.get("extended_entities"))
        favorite_count = from_union([from_int, from_none], obj.get("favorite_count"))
        favorited = from_union([from_bool, from_none], obj.get("favorited"))
        full_text = from_union([from_str, from_none], obj.get("full_text"))
        is_quote_status = from_union([from_bool, from_none], obj.get("is_quote_status"))
        lang = from_union([PurpleLang, from_none], obj.get("lang"))
        possibly_sensitive = from_union([from_bool, from_none], obj.get("possibly_sensitive"))
        possibly_sensitive_editable = from_union([from_bool, from_none], obj.get("possibly_sensitive_editable"))
        quote_count = from_union([from_int, from_none], obj.get("quote_count"))
        reply_count = from_union([from_int, from_none], obj.get("reply_count"))
        retweet_count = from_union([from_int, from_none], obj.get("retweet_count"))
        retweeted = from_union([from_bool, from_none], obj.get("retweeted"))
        id_str = from_union([from_str, from_none], obj.get("id_str"))
        return HilariousLegacy(user_id_str, bookmark_count, bookmarked, created_at, conversation_id_str, display_text_range, entities, extended_entities, favorite_count, favorited, full_text, is_quote_status, lang, possibly_sensitive, possibly_sensitive_editable, quote_count, reply_count, retweet_count, retweeted, id_str)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.user_id_str is not None:
            result["user_id_str"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.user_id_str)
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
            result["entities"] = from_union([lambda x: to_class(IndigoEntities, x), from_none], self.entities)
        if self.extended_entities is not None:
            result["extended_entities"] = from_union([lambda x: to_class(TentacledExtendedEntities, x), from_none], self.extended_entities)
        if self.favorite_count is not None:
            result["favorite_count"] = from_union([from_int, from_none], self.favorite_count)
        if self.favorited is not None:
            result["favorited"] = from_union([from_bool, from_none], self.favorited)
        if self.full_text is not None:
            result["full_text"] = from_union([from_str, from_none], self.full_text)
        if self.is_quote_status is not None:
            result["is_quote_status"] = from_union([from_bool, from_none], self.is_quote_status)
        if self.lang is not None:
            result["lang"] = from_union([lambda x: to_enum(PurpleLang, x), from_none], self.lang)
        if self.possibly_sensitive is not None:
            result["possibly_sensitive"] = from_union([from_bool, from_none], self.possibly_sensitive)
        if self.possibly_sensitive_editable is not None:
            result["possibly_sensitive_editable"] = from_union([from_bool, from_none], self.possibly_sensitive_editable)
        if self.quote_count is not None:
            result["quote_count"] = from_union([from_int, from_none], self.quote_count)
        if self.reply_count is not None:
            result["reply_count"] = from_union([from_int, from_none], self.reply_count)
        if self.retweet_count is not None:
            result["retweet_count"] = from_union([from_int, from_none], self.retweet_count)
        if self.retweeted is not None:
            result["retweeted"] = from_union([from_bool, from_none], self.retweeted)
        if self.id_str is not None:
            result["id_str"] = from_union([from_str, from_none], self.id_str)
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
class StickyResult:
    typename: Optional[TweetDisplayType] = None
    rest_id: Optional[str] = None
    has_birdwatch_notes: Optional[bool] = None
    core: Optional[TentacledCore] = None
    edit_control: Optional[EditControl] = None
    edit_perspective: Optional[EditPerspective] = None
    is_translatable: Optional[bool] = None
    views: Optional[Views] = None
    source: Optional[str] = None
    legacy: Optional[HilariousLegacy] = None

    @staticmethod
    def from_dict(obj: Any) -> 'StickyResult':
        assert isinstance(obj, dict)
        typename = from_union([TweetDisplayType, from_none], obj.get("__typename"))
        rest_id = from_union([from_str, from_none], obj.get("rest_id"))
        has_birdwatch_notes = from_union([from_bool, from_none], obj.get("has_birdwatch_notes"))
        core = from_union([TentacledCore.from_dict, from_none], obj.get("core"))
        edit_control = from_union([EditControl.from_dict, from_none], obj.get("edit_control"))
        edit_perspective = from_union([EditPerspective.from_dict, from_none], obj.get("edit_perspective"))
        is_translatable = from_union([from_bool, from_none], obj.get("is_translatable"))
        views = from_union([Views.from_dict, from_none], obj.get("views"))
        source = from_union([from_str, from_none], obj.get("source"))
        legacy = from_union([HilariousLegacy.from_dict, from_none], obj.get("legacy"))
        return StickyResult(typename, rest_id, has_birdwatch_notes, core, edit_control, edit_perspective, is_translatable, views, source, legacy)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.typename is not None:
            result["__typename"] = from_union([lambda x: to_enum(TweetDisplayType, x), from_none], self.typename)
        if self.rest_id is not None:
            result["rest_id"] = from_union([from_str, from_none], self.rest_id)
        if self.has_birdwatch_notes is not None:
            result["has_birdwatch_notes"] = from_union([from_bool, from_none], self.has_birdwatch_notes)
        if self.core is not None:
            result["core"] = from_union([lambda x: to_class(TentacledCore, x), from_none], self.core)
        if self.edit_control is not None:
            result["edit_control"] = from_union([lambda x: to_class(EditControl, x), from_none], self.edit_control)
        if self.edit_perspective is not None:
            result["edit_perspective"] = from_union([lambda x: to_class(EditPerspective, x), from_none], self.edit_perspective)
        if self.is_translatable is not None:
            result["is_translatable"] = from_union([from_bool, from_none], self.is_translatable)
        if self.views is not None:
            result["views"] = from_union([lambda x: to_class(Views, x), from_none], self.views)
        if self.source is not None:
            result["source"] = from_union([from_str, from_none], self.source)
        if self.legacy is not None:
            result["legacy"] = from_union([lambda x: to_class(HilariousLegacy, x), from_none], self.legacy)
        return result


@dataclass
class PurpleQuotedStatusResult:
    result: Optional[StickyResult] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PurpleQuotedStatusResult':
        assert isinstance(obj, dict)
        result = from_union([StickyResult.from_dict, from_none], obj.get("result"))
        return PurpleQuotedStatusResult(result)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.result is not None:
            result["result"] = from_union([lambda x: to_class(StickyResult, x), from_none], self.result)
        return result


@dataclass
class RetweetedStatusResultResult:
    typename: Optional[TweetDisplayType] = None
    rest_id: Optional[str] = None
    has_birdwatch_notes: Optional[bool] = None
    core: Optional[FluffyCore] = None
    edit_control: Optional[EditControl] = None
    edit_perspective: Optional[EditPerspective] = None
    is_translatable: Optional[bool] = None
    views: Optional[Views] = None
    source: Optional[str] = None
    legacy: Optional[IndigoLegacy] = None
    quoted_status_result: Optional[PurpleQuotedStatusResult] = None

    @staticmethod
    def from_dict(obj: Any) -> 'RetweetedStatusResultResult':
        assert isinstance(obj, dict)
        typename = from_union([TweetDisplayType, from_none], obj.get("__typename"))
        rest_id = from_union([from_str, from_none], obj.get("rest_id"))
        has_birdwatch_notes = from_union([from_bool, from_none], obj.get("has_birdwatch_notes"))
        core = from_union([FluffyCore.from_dict, from_none], obj.get("core"))
        edit_control = from_union([EditControl.from_dict, from_none], obj.get("edit_control"))
        edit_perspective = from_union([EditPerspective.from_dict, from_none], obj.get("edit_perspective"))
        is_translatable = from_union([from_bool, from_none], obj.get("is_translatable"))
        views = from_union([Views.from_dict, from_none], obj.get("views"))
        source = from_union([from_str, from_none], obj.get("source"))
        legacy = from_union([IndigoLegacy.from_dict, from_none], obj.get("legacy"))
        quoted_status_result = from_union([PurpleQuotedStatusResult.from_dict, from_none], obj.get("quoted_status_result"))
        return RetweetedStatusResultResult(typename, rest_id, has_birdwatch_notes, core, edit_control, edit_perspective, is_translatable, views, source, legacy, quoted_status_result)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.typename is not None:
            result["__typename"] = from_union([lambda x: to_enum(TweetDisplayType, x), from_none], self.typename)
        if self.rest_id is not None:
            result["rest_id"] = from_union([from_str, from_none], self.rest_id)
        if self.has_birdwatch_notes is not None:
            result["has_birdwatch_notes"] = from_union([from_bool, from_none], self.has_birdwatch_notes)
        if self.core is not None:
            result["core"] = from_union([lambda x: to_class(FluffyCore, x), from_none], self.core)
        if self.edit_control is not None:
            result["edit_control"] = from_union([lambda x: to_class(EditControl, x), from_none], self.edit_control)
        if self.edit_perspective is not None:
            result["edit_perspective"] = from_union([lambda x: to_class(EditPerspective, x), from_none], self.edit_perspective)
        if self.is_translatable is not None:
            result["is_translatable"] = from_union([from_bool, from_none], self.is_translatable)
        if self.views is not None:
            result["views"] = from_union([lambda x: to_class(Views, x), from_none], self.views)
        if self.source is not None:
            result["source"] = from_union([from_str, from_none], self.source)
        if self.legacy is not None:
            result["legacy"] = from_union([lambda x: to_class(IndigoLegacy, x), from_none], self.legacy)
        if self.quoted_status_result is not None:
            result["quoted_status_result"] = from_union([lambda x: to_class(PurpleQuotedStatusResult, x), from_none], self.quoted_status_result)
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
    lang: Optional[PurpleLang] = None
    quote_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None
    retweeted: Optional[bool] = None
    user_id_str: Optional[str] = None
    id_str: Optional[str] = None
    quoted_status_id_str: Optional[str] = None
    quoted_status_permalink: Optional[QuotedStatusPermalink] = None
    retweeted_status_result: Optional[RetweetedStatusResult] = None
    possibly_sensitive: Optional[bool] = None
    possibly_sensitive_editable: Optional[bool] = None
    extended_entities: Optional[PurpleExtendedEntities] = None

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
        lang = from_union([PurpleLang, from_none], obj.get("lang"))
        quote_count = from_union([from_int, from_none], obj.get("quote_count"))
        reply_count = from_union([from_int, from_none], obj.get("reply_count"))
        retweet_count = from_union([from_int, from_none], obj.get("retweet_count"))
        retweeted = from_union([from_bool, from_none], obj.get("retweeted"))
        user_id_str = from_union([from_str, from_none], obj.get("user_id_str"))
        id_str = from_union([from_str, from_none], obj.get("id_str"))
        quoted_status_id_str = from_union([from_str, from_none], obj.get("quoted_status_id_str"))
        quoted_status_permalink = from_union([QuotedStatusPermalink.from_dict, from_none], obj.get("quoted_status_permalink"))
        retweeted_status_result = from_union([RetweetedStatusResult.from_dict, from_none], obj.get("retweeted_status_result"))
        possibly_sensitive = from_union([from_bool, from_none], obj.get("possibly_sensitive"))
        possibly_sensitive_editable = from_union([from_bool, from_none], obj.get("possibly_sensitive_editable"))
        extended_entities = from_union([PurpleExtendedEntities.from_dict, from_none], obj.get("extended_entities"))
        return TentacledLegacy(bookmark_count, bookmarked, created_at, conversation_id_str, display_text_range, entities, favorite_count, favorited, full_text, is_quote_status, lang, quote_count, reply_count, retweet_count, retweeted, user_id_str, id_str, quoted_status_id_str, quoted_status_permalink, retweeted_status_result, possibly_sensitive, possibly_sensitive_editable, extended_entities)

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
            result["lang"] = from_union([lambda x: to_enum(PurpleLang, x), from_none], self.lang)
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
        if self.quoted_status_id_str is not None:
            result["quoted_status_id_str"] = from_union([from_str, from_none], self.quoted_status_id_str)
        if self.quoted_status_permalink is not None:
            result["quoted_status_permalink"] = from_union([lambda x: to_class(QuotedStatusPermalink, x), from_none], self.quoted_status_permalink)
        if self.retweeted_status_result is not None:
            result["retweeted_status_result"] = from_union([lambda x: to_class(RetweetedStatusResult, x), from_none], self.retweeted_status_result)
        if self.possibly_sensitive is not None:
            result["possibly_sensitive"] = from_union([from_bool, from_none], self.possibly_sensitive)
        if self.possibly_sensitive_editable is not None:
            result["possibly_sensitive_editable"] = from_union([from_bool, from_none], self.possibly_sensitive_editable)
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
class AmbitiousLegacy:
    can_dm: Optional[bool] = None
    can_media_tag: Optional[bool] = None
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
    profile_image_url_https: Optional[str] = None
    profile_interstitial_type: Optional[str] = None
    screen_name: Optional[ScreenName] = None
    statuses_count: Optional[int] = None
    translator_type: Optional[TranslatorType] = None
    url: Optional[str] = None
    verified: Optional[bool] = None
    want_retweets: Optional[bool] = None
    withheld_in_countries: Optional[List[Any]] = None
    profile_banner_url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AmbitiousLegacy':
        assert isinstance(obj, dict)
        can_dm = from_union([from_bool, from_none], obj.get("can_dm"))
        can_media_tag = from_union([from_bool, from_none], obj.get("can_media_tag"))
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
        profile_image_url_https = from_union([from_str, from_none], obj.get("profile_image_url_https"))
        profile_interstitial_type = from_union([from_str, from_none], obj.get("profile_interstitial_type"))
        screen_name = from_union([ScreenName, from_none], obj.get("screen_name"))
        statuses_count = from_union([from_int, from_none], obj.get("statuses_count"))
        translator_type = from_union([TranslatorType, from_none], obj.get("translator_type"))
        url = from_union([from_str, from_none], obj.get("url"))
        verified = from_union([from_bool, from_none], obj.get("verified"))
        want_retweets = from_union([from_bool, from_none], obj.get("want_retweets"))
        withheld_in_countries = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("withheld_in_countries"))
        profile_banner_url = from_union([from_str, from_none], obj.get("profile_banner_url"))
        return AmbitiousLegacy(can_dm, can_media_tag, created_at, default_profile, default_profile_image, description, entities, fast_followers_count, favourites_count, followers_count, friends_count, has_custom_timelines, is_translator, listed_count, location, media_count, name, normal_followers_count, pinned_tweet_ids_str, possibly_sensitive, profile_image_url_https, profile_interstitial_type, screen_name, statuses_count, translator_type, url, verified, want_retweets, withheld_in_countries, profile_banner_url)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.can_dm is not None:
            result["can_dm"] = from_union([from_bool, from_none], self.can_dm)
        if self.can_media_tag is not None:
            result["can_media_tag"] = from_union([from_bool, from_none], self.can_media_tag)
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
        if self.want_retweets is not None:
            result["want_retweets"] = from_union([from_bool, from_none], self.want_retweets)
        if self.withheld_in_countries is not None:
            result["withheld_in_countries"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.withheld_in_countries)
        if self.profile_banner_url is not None:
            result["profile_banner_url"] = from_union([from_str, from_none], self.profile_banner_url)
        return result


@dataclass
class HilariousResult:
    typename: Optional[UserDisplayTypeEnum] = None
    id: Optional[ID] = None
    rest_id: Optional[str] = None
    affiliates_highlighted_label: Optional[AffiliatesHighlightedLabel] = None
    has_graduated_access: Optional[bool] = None
    is_blue_verified: Optional[bool] = None
    profile_image_shape: Optional[ProfileImageShape] = None
    legacy: Optional[AmbitiousLegacy] = None
    smart_blocked_by: Optional[bool] = None
    smart_blocking: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'HilariousResult':
        assert isinstance(obj, dict)
        typename = from_union([UserDisplayTypeEnum, from_none], obj.get("__typename"))
        id = from_union([ID, from_none], obj.get("id"))
        rest_id = from_union([from_str, from_none], obj.get("rest_id"))
        affiliates_highlighted_label = from_union([AffiliatesHighlightedLabel.from_dict, from_none], obj.get("affiliates_highlighted_label"))
        has_graduated_access = from_union([from_bool, from_none], obj.get("has_graduated_access"))
        is_blue_verified = from_union([from_bool, from_none], obj.get("is_blue_verified"))
        profile_image_shape = from_union([ProfileImageShape, from_none], obj.get("profile_image_shape"))
        legacy = from_union([AmbitiousLegacy.from_dict, from_none], obj.get("legacy"))
        smart_blocked_by = from_union([from_bool, from_none], obj.get("smart_blocked_by"))
        smart_blocking = from_union([from_bool, from_none], obj.get("smart_blocking"))
        return HilariousResult(typename, id, rest_id, affiliates_highlighted_label, has_graduated_access, is_blue_verified, profile_image_shape, legacy, smart_blocked_by, smart_blocking)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.typename is not None:
            result["__typename"] = from_union([lambda x: to_enum(UserDisplayTypeEnum, x), from_none], self.typename)
        if self.id is not None:
            result["id"] = from_union([lambda x: to_enum(ID, x), from_none], self.id)
        if self.rest_id is not None:
            result["rest_id"] = from_union([from_str, from_none], self.rest_id)
        if self.affiliates_highlighted_label is not None:
            result["affiliates_highlighted_label"] = from_union([lambda x: to_class(AffiliatesHighlightedLabel, x), from_none], self.affiliates_highlighted_label)
        if self.has_graduated_access is not None:
            result["has_graduated_access"] = from_union([from_bool, from_none], self.has_graduated_access)
        if self.is_blue_verified is not None:
            result["is_blue_verified"] = from_union([from_bool, from_none], self.is_blue_verified)
        if self.profile_image_shape is not None:
            result["profile_image_shape"] = from_union([lambda x: to_enum(ProfileImageShape, x), from_none], self.profile_image_shape)
        if self.legacy is not None:
            result["legacy"] = from_union([lambda x: to_class(AmbitiousLegacy, x), from_none], self.legacy)
        if self.smart_blocked_by is not None:
            result["smart_blocked_by"] = from_union([from_bool, from_none], self.smart_blocked_by)
        if self.smart_blocking is not None:
            result["smart_blocking"] = from_union([from_bool, from_none], self.smart_blocking)
        return result


@dataclass
class StickyUserResults:
    result: Optional[HilariousResult] = None

    @staticmethod
    def from_dict(obj: Any) -> 'StickyUserResults':
        assert isinstance(obj, dict)
        result = from_union([HilariousResult.from_dict, from_none], obj.get("result"))
        return StickyUserResults(result)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.result is not None:
            result["result"] = from_union([lambda x: to_class(HilariousResult, x), from_none], self.result)
        return result


@dataclass
class StickyCore:
    user_results: Optional[StickyUserResults] = None

    @staticmethod
    def from_dict(obj: Any) -> 'StickyCore':
        assert isinstance(obj, dict)
        user_results = from_union([StickyUserResults.from_dict, from_none], obj.get("user_results"))
        return StickyCore(user_results)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.user_results is not None:
            result["user_results"] = from_union([lambda x: to_class(StickyUserResults, x), from_none], self.user_results)
        return result


@dataclass
class TentacledFeatures:
    large: Optional[FluffyLarge] = None
    medium: Optional[FluffyLarge] = None
    small: Optional[FluffyLarge] = None
    orig: Optional[FluffyLarge] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TentacledFeatures':
        assert isinstance(obj, dict)
        large = from_union([FluffyLarge.from_dict, from_none], obj.get("large"))
        medium = from_union([FluffyLarge.from_dict, from_none], obj.get("medium"))
        small = from_union([FluffyLarge.from_dict, from_none], obj.get("small"))
        orig = from_union([FluffyLarge.from_dict, from_none], obj.get("orig"))
        return TentacledFeatures(large, medium, small, orig)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.large is not None:
            result["large"] = from_union([lambda x: to_class(FluffyLarge, x), from_none], self.large)
        if self.medium is not None:
            result["medium"] = from_union([lambda x: to_class(FluffyLarge, x), from_none], self.medium)
        if self.small is not None:
            result["small"] = from_union([lambda x: to_class(FluffyLarge, x), from_none], self.small)
        if self.orig is not None:
            result["orig"] = from_union([lambda x: to_class(FluffyLarge, x), from_none], self.orig)
        return result


@dataclass
class HilariousMedia:
    display_url: Optional[str] = None
    expanded_url: Optional[str] = None
    id_str: Optional[str] = None
    indices: Optional[List[int]] = None
    media_url_https: Optional[str] = None
    type: Optional[MediaType] = None
    url: Optional[str] = None
    features: Optional[TentacledFeatures] = None
    sizes: Optional[Sizes] = None
    original_info: Optional[OriginalInfo] = None

    @staticmethod
    def from_dict(obj: Any) -> 'HilariousMedia':
        assert isinstance(obj, dict)
        display_url = from_union([from_str, from_none], obj.get("display_url"))
        expanded_url = from_union([from_str, from_none], obj.get("expanded_url"))
        id_str = from_union([from_str, from_none], obj.get("id_str"))
        indices = from_union([lambda x: from_list(from_int, x), from_none], obj.get("indices"))
        media_url_https = from_union([from_str, from_none], obj.get("media_url_https"))
        type = from_union([MediaType, from_none], obj.get("type"))
        url = from_union([from_str, from_none], obj.get("url"))
        features = from_union([TentacledFeatures.from_dict, from_none], obj.get("features"))
        sizes = from_union([Sizes.from_dict, from_none], obj.get("sizes"))
        original_info = from_union([OriginalInfo.from_dict, from_none], obj.get("original_info"))
        return HilariousMedia(display_url, expanded_url, id_str, indices, media_url_https, type, url, features, sizes, original_info)

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
            result["features"] = from_union([lambda x: to_class(TentacledFeatures, x), from_none], self.features)
        if self.sizes is not None:
            result["sizes"] = from_union([lambda x: to_class(Sizes, x), from_none], self.sizes)
        if self.original_info is not None:
            result["original_info"] = from_union([lambda x: to_class(OriginalInfo, x), from_none], self.original_info)
        return result


@dataclass
class IndecentEntities:
    user_mentions: Optional[List[Any]] = None
    urls: Optional[List[Any]] = None
    hashtags: Optional[List[Hashtag]] = None
    symbols: Optional[List[Any]] = None
    media: Optional[List[HilariousMedia]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'IndecentEntities':
        assert isinstance(obj, dict)
        user_mentions = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("user_mentions"))
        urls = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("urls"))
        hashtags = from_union([lambda x: from_list(Hashtag.from_dict, x), from_none], obj.get("hashtags"))
        symbols = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("symbols"))
        media = from_union([lambda x: from_list(HilariousMedia.from_dict, x), from_none], obj.get("media"))
        return IndecentEntities(user_mentions, urls, hashtags, symbols, media)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.user_mentions is not None:
            result["user_mentions"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.user_mentions)
        if self.urls is not None:
            result["urls"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.urls)
        if self.hashtags is not None:
            result["hashtags"] = from_union([lambda x: from_list(lambda x: to_class(Hashtag, x), x), from_none], self.hashtags)
        if self.symbols is not None:
            result["symbols"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.symbols)
        if self.media is not None:
            result["media"] = from_union([lambda x: from_list(lambda x: to_class(HilariousMedia, x), x), from_none], self.media)
        return result


@dataclass
class AmbitiousMedia:
    display_url: Optional[str] = None
    expanded_url: Optional[str] = None
    id_str: Optional[str] = None
    indices: Optional[List[int]] = None
    media_key: Optional[str] = None
    media_url_https: Optional[str] = None
    type: Optional[MediaType] = None
    url: Optional[str] = None
    ext_media_availability: Optional[EXTMediaAvailability] = None
    features: Optional[TentacledFeatures] = None
    sizes: Optional[Sizes] = None
    original_info: Optional[OriginalInfo] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AmbitiousMedia':
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
        features = from_union([TentacledFeatures.from_dict, from_none], obj.get("features"))
        sizes = from_union([Sizes.from_dict, from_none], obj.get("sizes"))
        original_info = from_union([OriginalInfo.from_dict, from_none], obj.get("original_info"))
        return AmbitiousMedia(display_url, expanded_url, id_str, indices, media_key, media_url_https, type, url, ext_media_availability, features, sizes, original_info)

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
            result["features"] = from_union([lambda x: to_class(TentacledFeatures, x), from_none], self.features)
        if self.sizes is not None:
            result["sizes"] = from_union([lambda x: to_class(Sizes, x), from_none], self.sizes)
        if self.original_info is not None:
            result["original_info"] = from_union([lambda x: to_class(OriginalInfo, x), from_none], self.original_info)
        return result


@dataclass
class StickyExtendedEntities:
    media: Optional[List[AmbitiousMedia]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'StickyExtendedEntities':
        assert isinstance(obj, dict)
        media = from_union([lambda x: from_list(AmbitiousMedia.from_dict, x), from_none], obj.get("media"))
        return StickyExtendedEntities(media)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.media is not None:
            result["media"] = from_union([lambda x: from_list(lambda x: to_class(AmbitiousMedia, x), x), from_none], self.media)
        return result


class FluffyLang(Enum):
    DA = "da"
    FI = "fi"
    NO = "no"
    ZXX = "zxx"


@dataclass
class CunningLegacy:
    bookmark_count: Optional[int] = None
    bookmarked: Optional[bool] = None
    created_at: Optional[str] = None
    conversation_id_str: Optional[str] = None
    display_text_range: Optional[List[int]] = None
    entities: Optional[IndecentEntities] = None
    favorite_count: Optional[int] = None
    favorited: Optional[bool] = None
    full_text: Optional[str] = None
    is_quote_status: Optional[bool] = None
    lang: Optional[FluffyLang] = None
    quote_count: Optional[int] = None
    quoted_status_id_str: Optional[str] = None
    quoted_status_permalink: Optional[QuotedStatusPermalink] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None
    retweeted: Optional[bool] = None
    user_id_str: Optional[str] = None
    id_str: Optional[str] = None
    extended_entities: Optional[StickyExtendedEntities] = None
    possibly_sensitive: Optional[bool] = None
    possibly_sensitive_editable: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'CunningLegacy':
        assert isinstance(obj, dict)
        bookmark_count = from_union([from_int, from_none], obj.get("bookmark_count"))
        bookmarked = from_union([from_bool, from_none], obj.get("bookmarked"))
        created_at = from_union([from_str, from_none], obj.get("created_at"))
        conversation_id_str = from_union([from_str, from_none], obj.get("conversation_id_str"))
        display_text_range = from_union([lambda x: from_list(from_int, x), from_none], obj.get("display_text_range"))
        entities = from_union([IndecentEntities.from_dict, from_none], obj.get("entities"))
        favorite_count = from_union([from_int, from_none], obj.get("favorite_count"))
        favorited = from_union([from_bool, from_none], obj.get("favorited"))
        full_text = from_union([from_str, from_none], obj.get("full_text"))
        is_quote_status = from_union([from_bool, from_none], obj.get("is_quote_status"))
        lang = from_union([FluffyLang, from_none], obj.get("lang"))
        quote_count = from_union([from_int, from_none], obj.get("quote_count"))
        quoted_status_id_str = from_union([from_str, from_none], obj.get("quoted_status_id_str"))
        quoted_status_permalink = from_union([QuotedStatusPermalink.from_dict, from_none], obj.get("quoted_status_permalink"))
        reply_count = from_union([from_int, from_none], obj.get("reply_count"))
        retweet_count = from_union([from_int, from_none], obj.get("retweet_count"))
        retweeted = from_union([from_bool, from_none], obj.get("retweeted"))
        user_id_str = from_union([from_str, from_none], obj.get("user_id_str"))
        id_str = from_union([from_str, from_none], obj.get("id_str"))
        extended_entities = from_union([StickyExtendedEntities.from_dict, from_none], obj.get("extended_entities"))
        possibly_sensitive = from_union([from_bool, from_none], obj.get("possibly_sensitive"))
        possibly_sensitive_editable = from_union([from_bool, from_none], obj.get("possibly_sensitive_editable"))
        return CunningLegacy(bookmark_count, bookmarked, created_at, conversation_id_str, display_text_range, entities, favorite_count, favorited, full_text, is_quote_status, lang, quote_count, quoted_status_id_str, quoted_status_permalink, reply_count, retweet_count, retweeted, user_id_str, id_str, extended_entities, possibly_sensitive, possibly_sensitive_editable)

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
            result["entities"] = from_union([lambda x: to_class(IndecentEntities, x), from_none], self.entities)
        if self.favorite_count is not None:
            result["favorite_count"] = from_union([from_int, from_none], self.favorite_count)
        if self.favorited is not None:
            result["favorited"] = from_union([from_bool, from_none], self.favorited)
        if self.full_text is not None:
            result["full_text"] = from_union([from_str, from_none], self.full_text)
        if self.is_quote_status is not None:
            result["is_quote_status"] = from_union([from_bool, from_none], self.is_quote_status)
        if self.lang is not None:
            result["lang"] = from_union([lambda x: to_enum(FluffyLang, x), from_none], self.lang)
        if self.quote_count is not None:
            result["quote_count"] = from_union([from_int, from_none], self.quote_count)
        if self.quoted_status_id_str is not None:
            result["quoted_status_id_str"] = from_union([from_str, from_none], self.quoted_status_id_str)
        if self.quoted_status_permalink is not None:
            result["quoted_status_permalink"] = from_union([lambda x: to_class(QuotedStatusPermalink, x), from_none], self.quoted_status_permalink)
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
        if self.extended_entities is not None:
            result["extended_entities"] = from_union([lambda x: to_class(StickyExtendedEntities, x), from_none], self.extended_entities)
        if self.possibly_sensitive is not None:
            result["possibly_sensitive"] = from_union([from_bool, from_none], self.possibly_sensitive)
        if self.possibly_sensitive_editable is not None:
            result["possibly_sensitive_editable"] = from_union([from_bool, from_none], self.possibly_sensitive_editable)
        return result


@dataclass
class QuotedRefResultResult:
    typename: Optional[TweetDisplayType] = None
    rest_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'QuotedRefResultResult':
        assert isinstance(obj, dict)
        typename = from_union([TweetDisplayType, from_none], obj.get("__typename"))
        rest_id = from_union([from_str, from_none], obj.get("rest_id"))
        return QuotedRefResultResult(typename, rest_id)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.typename is not None:
            result["__typename"] = from_union([lambda x: to_enum(TweetDisplayType, x), from_none], self.typename)
        if self.rest_id is not None:
            result["rest_id"] = from_union([from_str, from_none], self.rest_id)
        return result


@dataclass
class QuotedRefResult:
    result: Optional[QuotedRefResultResult] = None

    @staticmethod
    def from_dict(obj: Any) -> 'QuotedRefResult':
        assert isinstance(obj, dict)
        result = from_union([QuotedRefResultResult.from_dict, from_none], obj.get("result"))
        return QuotedRefResult(result)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.result is not None:
            result["result"] = from_union([lambda x: to_class(QuotedRefResultResult, x), from_none], self.result)
        return result


@dataclass
class IndecentResult:
    typename: Optional[TweetDisplayType] = None
    rest_id: Optional[str] = None
    has_birdwatch_notes: Optional[bool] = None
    core: Optional[StickyCore] = None
    edit_control: Optional[EditControl] = None
    edit_perspective: Optional[EditPerspective] = None
    is_translatable: Optional[bool] = None
    views: Optional[Views] = None
    source: Optional[str] = None
    quoted_ref_result: Optional[QuotedRefResult] = None
    legacy: Optional[CunningLegacy] = None

    @staticmethod
    def from_dict(obj: Any) -> 'IndecentResult':
        assert isinstance(obj, dict)
        typename = from_union([TweetDisplayType, from_none], obj.get("__typename"))
        rest_id = from_union([from_str, from_none], obj.get("rest_id"))
        has_birdwatch_notes = from_union([from_bool, from_none], obj.get("has_birdwatch_notes"))
        core = from_union([StickyCore.from_dict, from_none], obj.get("core"))
        edit_control = from_union([EditControl.from_dict, from_none], obj.get("edit_control"))
        edit_perspective = from_union([EditPerspective.from_dict, from_none], obj.get("edit_perspective"))
        is_translatable = from_union([from_bool, from_none], obj.get("is_translatable"))
        views = from_union([Views.from_dict, from_none], obj.get("views"))
        source = from_union([from_str, from_none], obj.get("source"))
        quoted_ref_result = from_union([QuotedRefResult.from_dict, from_none], obj.get("quotedRefResult"))
        legacy = from_union([CunningLegacy.from_dict, from_none], obj.get("legacy"))
        return IndecentResult(typename, rest_id, has_birdwatch_notes, core, edit_control, edit_perspective, is_translatable, views, source, quoted_ref_result, legacy)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.typename is not None:
            result["__typename"] = from_union([lambda x: to_enum(TweetDisplayType, x), from_none], self.typename)
        if self.rest_id is not None:
            result["rest_id"] = from_union([from_str, from_none], self.rest_id)
        if self.has_birdwatch_notes is not None:
            result["has_birdwatch_notes"] = from_union([from_bool, from_none], self.has_birdwatch_notes)
        if self.core is not None:
            result["core"] = from_union([lambda x: to_class(StickyCore, x), from_none], self.core)
        if self.edit_control is not None:
            result["edit_control"] = from_union([lambda x: to_class(EditControl, x), from_none], self.edit_control)
        if self.edit_perspective is not None:
            result["edit_perspective"] = from_union([lambda x: to_class(EditPerspective, x), from_none], self.edit_perspective)
        if self.is_translatable is not None:
            result["is_translatable"] = from_union([from_bool, from_none], self.is_translatable)
        if self.views is not None:
            result["views"] = from_union([lambda x: to_class(Views, x), from_none], self.views)
        if self.source is not None:
            result["source"] = from_union([from_str, from_none], self.source)
        if self.quoted_ref_result is not None:
            result["quotedRefResult"] = from_union([lambda x: to_class(QuotedRefResult, x), from_none], self.quoted_ref_result)
        if self.legacy is not None:
            result["legacy"] = from_union([lambda x: to_class(CunningLegacy, x), from_none], self.legacy)
        return result


@dataclass
class FluffyQuotedStatusResult:
    result: Optional[IndecentResult] = None

    @staticmethod
    def from_dict(obj: Any) -> 'FluffyQuotedStatusResult':
        assert isinstance(obj, dict)
        result = from_union([IndecentResult.from_dict, from_none], obj.get("result"))
        return FluffyQuotedStatusResult(result)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.result is not None:
            result["result"] = from_union([lambda x: to_class(IndecentResult, x), from_none], self.result)
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
class PurpleResult:
    typename: Optional[TweetDisplayType] = None
    rest_id: Optional[str] = None
    has_birdwatch_notes: Optional[bool] = None
    core: Optional[PurpleCore] = None
    edit_control: Optional[EditControl] = None
    edit_perspective: Optional[EditPerspective] = None
    is_translatable: Optional[bool] = None
    views: Optional[Views] = None
    source: Optional[str] = None
    legacy: Optional[TentacledLegacy] = None
    quick_promote_eligibility: Optional[QuickPromoteEligibility] = None
    quoted_status_result: Optional[FluffyQuotedStatusResult] = None
    card: Optional[PurpleCard] = None
    unified_card: Optional[UnifiedCard] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PurpleResult':
        assert isinstance(obj, dict)
        typename = from_union([TweetDisplayType, from_none], obj.get("__typename"))
        rest_id = from_union([from_str, from_none], obj.get("rest_id"))
        has_birdwatch_notes = from_union([from_bool, from_none], obj.get("has_birdwatch_notes"))
        core = from_union([PurpleCore.from_dict, from_none], obj.get("core"))
        edit_control = from_union([EditControl.from_dict, from_none], obj.get("edit_control"))
        edit_perspective = from_union([EditPerspective.from_dict, from_none], obj.get("edit_perspective"))
        is_translatable = from_union([from_bool, from_none], obj.get("is_translatable"))
        views = from_union([Views.from_dict, from_none], obj.get("views"))
        source = from_union([from_str, from_none], obj.get("source"))
        legacy = from_union([TentacledLegacy.from_dict, from_none], obj.get("legacy"))
        quick_promote_eligibility = from_union([QuickPromoteEligibility.from_dict, from_none], obj.get("quick_promote_eligibility"))
        quoted_status_result = from_union([FluffyQuotedStatusResult.from_dict, from_none], obj.get("quoted_status_result"))
        card = from_union([PurpleCard.from_dict, from_none], obj.get("card"))
        unified_card = from_union([UnifiedCard.from_dict, from_none], obj.get("unified_card"))
        return PurpleResult(typename, rest_id, has_birdwatch_notes, core, edit_control, edit_perspective, is_translatable, views, source, legacy, quick_promote_eligibility, quoted_status_result, card, unified_card)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.typename is not None:
            result["__typename"] = from_union([lambda x: to_enum(TweetDisplayType, x), from_none], self.typename)
        if self.rest_id is not None:
            result["rest_id"] = from_union([from_str, from_none], self.rest_id)
        if self.has_birdwatch_notes is not None:
            result["has_birdwatch_notes"] = from_union([from_bool, from_none], self.has_birdwatch_notes)
        if self.core is not None:
            result["core"] = from_union([lambda x: to_class(PurpleCore, x), from_none], self.core)
        if self.edit_control is not None:
            result["edit_control"] = from_union([lambda x: to_class(EditControl, x), from_none], self.edit_control)
        if self.edit_perspective is not None:
            result["edit_perspective"] = from_union([lambda x: to_class(EditPerspective, x), from_none], self.edit_perspective)
        if self.is_translatable is not None:
            result["is_translatable"] = from_union([from_bool, from_none], self.is_translatable)
        if self.views is not None:
            result["views"] = from_union([lambda x: to_class(Views, x), from_none], self.views)
        if self.source is not None:
            result["source"] = from_union([from_str, from_none], self.source)
        if self.legacy is not None:
            result["legacy"] = from_union([lambda x: to_class(TentacledLegacy, x), from_none], self.legacy)
        if self.quick_promote_eligibility is not None:
            result["quick_promote_eligibility"] = from_union([lambda x: to_class(QuickPromoteEligibility, x), from_none], self.quick_promote_eligibility)
        if self.quoted_status_result is not None:
            result["quoted_status_result"] = from_union([lambda x: to_class(FluffyQuotedStatusResult, x), from_none], self.quoted_status_result)
        if self.card is not None:
            result["card"] = from_union([lambda x: to_class(PurpleCard, x), from_none], self.card)
        if self.unified_card is not None:
            result["unified_card"] = from_union([lambda x: to_class(UnifiedCard, x), from_none], self.unified_card)
        return result


@dataclass
class PurpleTweetResults:
    result: Optional[PurpleResult] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PurpleTweetResults':
        assert isinstance(obj, dict)
        result = from_union([PurpleResult.from_dict, from_none], obj.get("result"))
        return PurpleTweetResults(result)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.result is not None:
            result["result"] = from_union([lambda x: to_class(PurpleResult, x), from_none], self.result)
        return result


@dataclass
class ContentItemContent:
    item_type: Optional[ItemTypeEnum] = None
    typename: Optional[ItemTypeEnum] = None
    tweet_results: Optional[PurpleTweetResults] = None
    tweet_display_type: Optional[TweetDisplayType] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ContentItemContent':
        assert isinstance(obj, dict)
        item_type = from_union([ItemTypeEnum, from_none], obj.get("itemType"))
        typename = from_union([ItemTypeEnum, from_none], obj.get("__typename"))
        tweet_results = from_union([PurpleTweetResults.from_dict, from_none], obj.get("tweet_results"))
        tweet_display_type = from_union([TweetDisplayType, from_none], obj.get("tweetDisplayType"))
        return ContentItemContent(item_type, typename, tweet_results, tweet_display_type)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.item_type is not None:
            result["itemType"] = from_union([lambda x: to_enum(ItemTypeEnum, x), from_none], self.item_type)
        if self.typename is not None:
            result["__typename"] = from_union([lambda x: to_enum(ItemTypeEnum, x), from_none], self.typename)
        if self.tweet_results is not None:
            result["tweet_results"] = from_union([lambda x: to_class(PurpleTweetResults, x), from_none], self.tweet_results)
        if self.tweet_display_type is not None:
            result["tweetDisplayType"] = from_union([lambda x: to_enum(TweetDisplayType, x), from_none], self.tweet_display_type)
        return result


@dataclass
class ItemClientEventInfo:
    component: Optional[Ent] = None
    element: Optional[Element] = None
    details: Optional[Details] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ItemClientEventInfo':
        assert isinstance(obj, dict)
        component = from_union([Ent, from_none], obj.get("component"))
        element = from_union([Element, from_none], obj.get("element"))
        details = from_union([Details.from_dict, from_none], obj.get("details"))
        return ItemClientEventInfo(component, element, details)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.component is not None:
            result["component"] = from_union([lambda x: to_enum(Ent, x), from_none], self.component)
        if self.element is not None:
            result["element"] = from_union([lambda x: to_enum(Element, x), from_none], self.element)
        if self.details is not None:
            result["details"] = from_union([lambda x: to_class(Details, x), from_none], self.details)
        return result


@dataclass
class FluffyValue:
    string_value: Optional[str] = None
    type: Optional[ValueType] = None
    scribe_key: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'FluffyValue':
        assert isinstance(obj, dict)
        string_value = from_union([from_str, from_none], obj.get("string_value"))
        type = from_union([ValueType, from_none], obj.get("type"))
        scribe_key = from_union([from_str, from_none], obj.get("scribe_key"))
        return FluffyValue(string_value, type, scribe_key)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.string_value is not None:
            result["string_value"] = from_union([from_str, from_none], self.string_value)
        if self.type is not None:
            result["type"] = from_union([lambda x: to_enum(ValueType, x), from_none], self.type)
        if self.scribe_key is not None:
            result["scribe_key"] = from_union([from_str, from_none], self.scribe_key)
        return result


@dataclass
class FluffyBindingValue:
    key: Optional[str] = None
    value: Optional[FluffyValue] = None

    @staticmethod
    def from_dict(obj: Any) -> 'FluffyBindingValue':
        assert isinstance(obj, dict)
        key = from_union([from_str, from_none], obj.get("key"))
        value = from_union([FluffyValue.from_dict, from_none], obj.get("value"))
        return FluffyBindingValue(key, value)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.key is not None:
            result["key"] = from_union([from_str, from_none], self.key)
        if self.value is not None:
            result["value"] = from_union([lambda x: to_class(FluffyValue, x), from_none], self.value)
        return result


@dataclass
class MagentaLegacy:
    binding_values: Optional[List[FluffyBindingValue]] = None
    card_platform: Optional[CardPlatform] = None
    name: Optional[str] = None
    url: Optional[str] = None
    user_refs_results: Optional[List[Any]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'MagentaLegacy':
        assert isinstance(obj, dict)
        binding_values = from_union([lambda x: from_list(FluffyBindingValue.from_dict, x), from_none], obj.get("binding_values"))
        card_platform = from_union([CardPlatform.from_dict, from_none], obj.get("card_platform"))
        name = from_union([from_str, from_none], obj.get("name"))
        url = from_union([from_str, from_none], obj.get("url"))
        user_refs_results = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("user_refs_results"))
        return MagentaLegacy(binding_values, card_platform, name, url, user_refs_results)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.binding_values is not None:
            result["binding_values"] = from_union([lambda x: from_list(lambda x: to_class(FluffyBindingValue, x), x), from_none], self.binding_values)
        if self.card_platform is not None:
            result["card_platform"] = from_union([lambda x: to_class(CardPlatform, x), from_none], self.card_platform)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.url is not None:
            result["url"] = from_union([from_str, from_none], self.url)
        if self.user_refs_results is not None:
            result["user_refs_results"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.user_refs_results)
        return result


@dataclass
class FluffyCard:
    rest_id: Optional[str] = None
    legacy: Optional[MagentaLegacy] = None

    @staticmethod
    def from_dict(obj: Any) -> 'FluffyCard':
        assert isinstance(obj, dict)
        rest_id = from_union([from_str, from_none], obj.get("rest_id"))
        legacy = from_union([MagentaLegacy.from_dict, from_none], obj.get("legacy"))
        return FluffyCard(rest_id, legacy)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.rest_id is not None:
            result["rest_id"] = from_union([from_str, from_none], self.rest_id)
        if self.legacy is not None:
            result["legacy"] = from_union([lambda x: to_class(MagentaLegacy, x), from_none], self.legacy)
        return result


@dataclass
class FriskyLegacy:
    can_dm: Optional[bool] = None
    can_media_tag: Optional[bool] = None
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
    pinned_tweet_ids_str: Optional[List[Any]] = None
    possibly_sensitive: Optional[bool] = None
    profile_image_url_https: Optional[str] = None
    profile_interstitial_type: Optional[str] = None
    screen_name: Optional[ScreenName] = None
    statuses_count: Optional[int] = None
    translator_type: Optional[TranslatorType] = None
    url: Optional[str] = None
    verified: Optional[bool] = None
    want_retweets: Optional[bool] = None
    withheld_in_countries: Optional[List[Any]] = None
    profile_banner_url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'FriskyLegacy':
        assert isinstance(obj, dict)
        can_dm = from_union([from_bool, from_none], obj.get("can_dm"))
        can_media_tag = from_union([from_bool, from_none], obj.get("can_media_tag"))
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
        pinned_tweet_ids_str = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("pinned_tweet_ids_str"))
        possibly_sensitive = from_union([from_bool, from_none], obj.get("possibly_sensitive"))
        profile_image_url_https = from_union([from_str, from_none], obj.get("profile_image_url_https"))
        profile_interstitial_type = from_union([from_str, from_none], obj.get("profile_interstitial_type"))
        screen_name = from_union([ScreenName, from_none], obj.get("screen_name"))
        statuses_count = from_union([from_int, from_none], obj.get("statuses_count"))
        translator_type = from_union([TranslatorType, from_none], obj.get("translator_type"))
        url = from_union([from_str, from_none], obj.get("url"))
        verified = from_union([from_bool, from_none], obj.get("verified"))
        want_retweets = from_union([from_bool, from_none], obj.get("want_retweets"))
        withheld_in_countries = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("withheld_in_countries"))
        profile_banner_url = from_union([from_str, from_none], obj.get("profile_banner_url"))
        return FriskyLegacy(can_dm, can_media_tag, created_at, default_profile, default_profile_image, description, entities, fast_followers_count, favourites_count, followers_count, friends_count, has_custom_timelines, is_translator, listed_count, location, media_count, name, normal_followers_count, pinned_tweet_ids_str, possibly_sensitive, profile_image_url_https, profile_interstitial_type, screen_name, statuses_count, translator_type, url, verified, want_retweets, withheld_in_countries, profile_banner_url)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.can_dm is not None:
            result["can_dm"] = from_union([from_bool, from_none], self.can_dm)
        if self.can_media_tag is not None:
            result["can_media_tag"] = from_union([from_bool, from_none], self.can_media_tag)
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
            result["pinned_tweet_ids_str"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.pinned_tweet_ids_str)
        if self.possibly_sensitive is not None:
            result["possibly_sensitive"] = from_union([from_bool, from_none], self.possibly_sensitive)
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
        if self.want_retweets is not None:
            result["want_retweets"] = from_union([from_bool, from_none], self.want_retweets)
        if self.withheld_in_countries is not None:
            result["withheld_in_countries"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.withheld_in_countries)
        if self.profile_banner_url is not None:
            result["profile_banner_url"] = from_union([from_str, from_none], self.profile_banner_url)
        return result


@dataclass
class CunningResult:
    typename: Optional[UserDisplayTypeEnum] = None
    id: Optional[ID] = None
    rest_id: Optional[str] = None
    affiliates_highlighted_label: Optional[AffiliatesHighlightedLabel] = None
    has_graduated_access: Optional[bool] = None
    is_blue_verified: Optional[bool] = None
    profile_image_shape: Optional[ProfileImageShape] = None
    legacy: Optional[FriskyLegacy] = None
    smart_blocked_by: Optional[bool] = None
    smart_blocking: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'CunningResult':
        assert isinstance(obj, dict)
        typename = from_union([UserDisplayTypeEnum, from_none], obj.get("__typename"))
        id = from_union([ID, from_none], obj.get("id"))
        rest_id = from_union([from_str, from_none], obj.get("rest_id"))
        affiliates_highlighted_label = from_union([AffiliatesHighlightedLabel.from_dict, from_none], obj.get("affiliates_highlighted_label"))
        has_graduated_access = from_union([from_bool, from_none], obj.get("has_graduated_access"))
        is_blue_verified = from_union([from_bool, from_none], obj.get("is_blue_verified"))
        profile_image_shape = from_union([ProfileImageShape, from_none], obj.get("profile_image_shape"))
        legacy = from_union([FriskyLegacy.from_dict, from_none], obj.get("legacy"))
        smart_blocked_by = from_union([from_bool, from_none], obj.get("smart_blocked_by"))
        smart_blocking = from_union([from_bool, from_none], obj.get("smart_blocking"))
        return CunningResult(typename, id, rest_id, affiliates_highlighted_label, has_graduated_access, is_blue_verified, profile_image_shape, legacy, smart_blocked_by, smart_blocking)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.typename is not None:
            result["__typename"] = from_union([lambda x: to_enum(UserDisplayTypeEnum, x), from_none], self.typename)
        if self.id is not None:
            result["id"] = from_union([lambda x: to_enum(ID, x), from_none], self.id)
        if self.rest_id is not None:
            result["rest_id"] = from_union([from_str, from_none], self.rest_id)
        if self.affiliates_highlighted_label is not None:
            result["affiliates_highlighted_label"] = from_union([lambda x: to_class(AffiliatesHighlightedLabel, x), from_none], self.affiliates_highlighted_label)
        if self.has_graduated_access is not None:
            result["has_graduated_access"] = from_union([from_bool, from_none], self.has_graduated_access)
        if self.is_blue_verified is not None:
            result["is_blue_verified"] = from_union([from_bool, from_none], self.is_blue_verified)
        if self.profile_image_shape is not None:
            result["profile_image_shape"] = from_union([lambda x: to_enum(ProfileImageShape, x), from_none], self.profile_image_shape)
        if self.legacy is not None:
            result["legacy"] = from_union([lambda x: to_class(FriskyLegacy, x), from_none], self.legacy)
        if self.smart_blocked_by is not None:
            result["smart_blocked_by"] = from_union([from_bool, from_none], self.smart_blocked_by)
        if self.smart_blocking is not None:
            result["smart_blocking"] = from_union([from_bool, from_none], self.smart_blocking)
        return result


@dataclass
class IndigoUserResults:
    result: Optional[CunningResult] = None

    @staticmethod
    def from_dict(obj: Any) -> 'IndigoUserResults':
        assert isinstance(obj, dict)
        result = from_union([CunningResult.from_dict, from_none], obj.get("result"))
        return IndigoUserResults(result)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.result is not None:
            result["result"] = from_union([lambda x: to_class(CunningResult, x), from_none], self.result)
        return result


@dataclass
class IndigoCore:
    user_results: Optional[IndigoUserResults] = None

    @staticmethod
    def from_dict(obj: Any) -> 'IndigoCore':
        assert isinstance(obj, dict)
        user_results = from_union([IndigoUserResults.from_dict, from_none], obj.get("user_results"))
        return IndigoCore(user_results)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.user_results is not None:
            result["user_results"] = from_union([lambda x: to_class(IndigoUserResults, x), from_none], self.user_results)
        return result


@dataclass
class IndigoURL:
    display_url: Optional[str] = None
    expanded_url: Optional[str] = None
    url: Optional[str] = None
    indices: Optional[List[int]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'IndigoURL':
        assert isinstance(obj, dict)
        display_url = from_union([from_str, from_none], obj.get("display_url"))
        expanded_url = from_union([from_str, from_none], obj.get("expanded_url"))
        url = from_union([from_str, from_none], obj.get("url"))
        indices = from_union([lambda x: from_list(from_int, x), from_none], obj.get("indices"))
        return IndigoURL(display_url, expanded_url, url, indices)

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
class TentacledUserMention:
    id_str: Optional[int] = None
    name: Optional[Name] = None
    screen_name: Optional[ScreenName] = None
    indices: Optional[List[int]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TentacledUserMention':
        assert isinstance(obj, dict)
        id_str = from_union([from_none, lambda x: int(from_str(x))], obj.get("id_str"))
        name = from_union([Name, from_none], obj.get("name"))
        screen_name = from_union([ScreenName, from_none], obj.get("screen_name"))
        indices = from_union([lambda x: from_list(from_int, x), from_none], obj.get("indices"))
        return TentacledUserMention(id_str, name, screen_name, indices)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.id_str is not None:
            result["id_str"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.id_str)
        if self.name is not None:
            result["name"] = from_union([lambda x: to_enum(Name, x), from_none], self.name)
        if self.screen_name is not None:
            result["screen_name"] = from_union([lambda x: to_enum(ScreenName, x), from_none], self.screen_name)
        if self.indices is not None:
            result["indices"] = from_union([lambda x: from_list(from_int, x), from_none], self.indices)
        return result


@dataclass
class HilariousEntities:
    user_mentions: Optional[List[TentacledUserMention]] = None
    urls: Optional[List[IndigoURL]] = None
    hashtags: Optional[List[Hashtag]] = None
    symbols: Optional[List[Any]] = None
    media: Optional[List[PurpleMedia]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'HilariousEntities':
        assert isinstance(obj, dict)
        user_mentions = from_union([lambda x: from_list(TentacledUserMention.from_dict, x), from_none], obj.get("user_mentions"))
        urls = from_union([lambda x: from_list(IndigoURL.from_dict, x), from_none], obj.get("urls"))
        hashtags = from_union([lambda x: from_list(Hashtag.from_dict, x), from_none], obj.get("hashtags"))
        symbols = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("symbols"))
        media = from_union([lambda x: from_list(PurpleMedia.from_dict, x), from_none], obj.get("media"))
        return HilariousEntities(user_mentions, urls, hashtags, symbols, media)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.user_mentions is not None:
            result["user_mentions"] = from_union([lambda x: from_list(lambda x: to_class(TentacledUserMention, x), x), from_none], self.user_mentions)
        if self.urls is not None:
            result["urls"] = from_union([lambda x: from_list(lambda x: to_class(IndigoURL, x), x), from_none], self.urls)
        if self.hashtags is not None:
            result["hashtags"] = from_union([lambda x: from_list(lambda x: to_class(Hashtag, x), x), from_none], self.hashtags)
        if self.symbols is not None:
            result["symbols"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.symbols)
        if self.media is not None:
            result["media"] = from_union([lambda x: from_list(lambda x: to_class(PurpleMedia, x), x), from_none], self.media)
        return result


@dataclass
class CunningMedia:
    display_url: Optional[str] = None
    expanded_url: Optional[str] = None
    id_str: Optional[str] = None
    indices: Optional[List[int]] = None
    media_key: Optional[str] = None
    media_url_https: Optional[str] = None
    type: Optional[MediaType] = None
    url: Optional[str] = None
    ext_media_availability: Optional[EXTMediaAvailability] = None
    features: Optional[PurpleFeatures] = None
    sizes: Optional[Sizes] = None
    original_info: Optional[OriginalInfo] = None
    video_info: Optional[VideoInfo] = None

    @staticmethod
    def from_dict(obj: Any) -> 'CunningMedia':
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
        features = from_union([PurpleFeatures.from_dict, from_none], obj.get("features"))
        sizes = from_union([Sizes.from_dict, from_none], obj.get("sizes"))
        original_info = from_union([OriginalInfo.from_dict, from_none], obj.get("original_info"))
        video_info = from_union([VideoInfo.from_dict, from_none], obj.get("video_info"))
        return CunningMedia(display_url, expanded_url, id_str, indices, media_key, media_url_https, type, url, ext_media_availability, features, sizes, original_info, video_info)

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
            result["features"] = from_union([lambda x: to_class(PurpleFeatures, x), from_none], self.features)
        if self.sizes is not None:
            result["sizes"] = from_union([lambda x: to_class(Sizes, x), from_none], self.sizes)
        if self.original_info is not None:
            result["original_info"] = from_union([lambda x: to_class(OriginalInfo, x), from_none], self.original_info)
        if self.video_info is not None:
            result["video_info"] = from_union([lambda x: to_class(VideoInfo, x), from_none], self.video_info)
        return result


@dataclass
class IndigoExtendedEntities:
    media: Optional[List[CunningMedia]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'IndigoExtendedEntities':
        assert isinstance(obj, dict)
        media = from_union([lambda x: from_list(CunningMedia.from_dict, x), from_none], obj.get("media"))
        return IndigoExtendedEntities(media)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.media is not None:
            result["media"] = from_union([lambda x: from_list(lambda x: to_class(CunningMedia, x), x), from_none], self.media)
        return result


@dataclass
class MischievousLegacy:
    bookmark_count: Optional[int] = None
    bookmarked: Optional[bool] = None
    created_at: Optional[str] = None
    conversation_id_str: Optional[str] = None
    display_text_range: Optional[List[int]] = None
    entities: Optional[HilariousEntities] = None
    favorite_count: Optional[int] = None
    favorited: Optional[bool] = None
    full_text: Optional[str] = None
    is_quote_status: Optional[bool] = None
    lang: Optional[FluffyLang] = None
    quote_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None
    retweeted: Optional[bool] = None
    user_id_str: Optional[str] = None
    id_str: Optional[str] = None
    in_reply_to_screen_name: Optional[ScreenName] = None
    in_reply_to_status_id_str: Optional[str] = None
    in_reply_to_user_id_str: Optional[str] = None
    possibly_sensitive: Optional[bool] = None
    possibly_sensitive_editable: Optional[bool] = None
    extended_entities: Optional[IndigoExtendedEntities] = None
    quoted_status_id_str: Optional[str] = None
    quoted_status_permalink: Optional[QuotedStatusPermalink] = None

    @staticmethod
    def from_dict(obj: Any) -> 'MischievousLegacy':
        assert isinstance(obj, dict)
        bookmark_count = from_union([from_int, from_none], obj.get("bookmark_count"))
        bookmarked = from_union([from_bool, from_none], obj.get("bookmarked"))
        created_at = from_union([from_str, from_none], obj.get("created_at"))
        conversation_id_str = from_union([from_str, from_none], obj.get("conversation_id_str"))
        display_text_range = from_union([lambda x: from_list(from_int, x), from_none], obj.get("display_text_range"))
        entities = from_union([HilariousEntities.from_dict, from_none], obj.get("entities"))
        favorite_count = from_union([from_int, from_none], obj.get("favorite_count"))
        favorited = from_union([from_bool, from_none], obj.get("favorited"))
        full_text = from_union([from_str, from_none], obj.get("full_text"))
        is_quote_status = from_union([from_bool, from_none], obj.get("is_quote_status"))
        lang = from_union([FluffyLang, from_none], obj.get("lang"))
        quote_count = from_union([from_int, from_none], obj.get("quote_count"))
        reply_count = from_union([from_int, from_none], obj.get("reply_count"))
        retweet_count = from_union([from_int, from_none], obj.get("retweet_count"))
        retweeted = from_union([from_bool, from_none], obj.get("retweeted"))
        user_id_str = from_union([from_str, from_none], obj.get("user_id_str"))
        id_str = from_union([from_str, from_none], obj.get("id_str"))
        in_reply_to_screen_name = from_union([ScreenName, from_none], obj.get("in_reply_to_screen_name"))
        in_reply_to_status_id_str = from_union([from_str, from_none], obj.get("in_reply_to_status_id_str"))
        in_reply_to_user_id_str = from_union([from_str, from_none], obj.get("in_reply_to_user_id_str"))
        possibly_sensitive = from_union([from_bool, from_none], obj.get("possibly_sensitive"))
        possibly_sensitive_editable = from_union([from_bool, from_none], obj.get("possibly_sensitive_editable"))
        extended_entities = from_union([IndigoExtendedEntities.from_dict, from_none], obj.get("extended_entities"))
        quoted_status_id_str = from_union([from_str, from_none], obj.get("quoted_status_id_str"))
        quoted_status_permalink = from_union([QuotedStatusPermalink.from_dict, from_none], obj.get("quoted_status_permalink"))
        return MischievousLegacy(bookmark_count, bookmarked, created_at, conversation_id_str, display_text_range, entities, favorite_count, favorited, full_text, is_quote_status, lang, quote_count, reply_count, retweet_count, retweeted, user_id_str, id_str, in_reply_to_screen_name, in_reply_to_status_id_str, in_reply_to_user_id_str, possibly_sensitive, possibly_sensitive_editable, extended_entities, quoted_status_id_str, quoted_status_permalink)

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
            result["entities"] = from_union([lambda x: to_class(HilariousEntities, x), from_none], self.entities)
        if self.favorite_count is not None:
            result["favorite_count"] = from_union([from_int, from_none], self.favorite_count)
        if self.favorited is not None:
            result["favorited"] = from_union([from_bool, from_none], self.favorited)
        if self.full_text is not None:
            result["full_text"] = from_union([from_str, from_none], self.full_text)
        if self.is_quote_status is not None:
            result["is_quote_status"] = from_union([from_bool, from_none], self.is_quote_status)
        if self.lang is not None:
            result["lang"] = from_union([lambda x: to_enum(FluffyLang, x), from_none], self.lang)
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
        if self.in_reply_to_screen_name is not None:
            result["in_reply_to_screen_name"] = from_union([lambda x: to_enum(ScreenName, x), from_none], self.in_reply_to_screen_name)
        if self.in_reply_to_status_id_str is not None:
            result["in_reply_to_status_id_str"] = from_union([from_str, from_none], self.in_reply_to_status_id_str)
        if self.in_reply_to_user_id_str is not None:
            result["in_reply_to_user_id_str"] = from_union([from_str, from_none], self.in_reply_to_user_id_str)
        if self.possibly_sensitive is not None:
            result["possibly_sensitive"] = from_union([from_bool, from_none], self.possibly_sensitive)
        if self.possibly_sensitive_editable is not None:
            result["possibly_sensitive_editable"] = from_union([from_bool, from_none], self.possibly_sensitive_editable)
        if self.extended_entities is not None:
            result["extended_entities"] = from_union([lambda x: to_class(IndigoExtendedEntities, x), from_none], self.extended_entities)
        if self.quoted_status_id_str is not None:
            result["quoted_status_id_str"] = from_union([from_str, from_none], self.quoted_status_id_str)
        if self.quoted_status_permalink is not None:
            result["quoted_status_permalink"] = from_union([lambda x: to_class(QuotedStatusPermalink, x), from_none], self.quoted_status_permalink)
        return result


@dataclass
class BraggadociousLegacy:
    can_dm: Optional[bool] = None
    can_media_tag: Optional[bool] = None
    created_at: Optional[str] = None
    default_profile: Optional[bool] = None
    default_profile_image: Optional[bool] = None
    description: Optional[str] = None
    entities: Optional[TentacledEntities] = None
    fast_followers_count: Optional[int] = None
    favourites_count: Optional[int] = None
    followers_count: Optional[int] = None
    friends_count: Optional[int] = None
    has_custom_timelines: Optional[bool] = None
    is_translator: Optional[bool] = None
    listed_count: Optional[int] = None
    location: Optional[str] = None
    media_count: Optional[int] = None
    name: Optional[str] = None
    normal_followers_count: Optional[int] = None
    pinned_tweet_ids_str: Optional[List[Any]] = None
    possibly_sensitive: Optional[bool] = None
    profile_banner_url: Optional[str] = None
    profile_image_url_https: Optional[str] = None
    profile_interstitial_type: Optional[str] = None
    screen_name: Optional[str] = None
    statuses_count: Optional[int] = None
    translator_type: Optional[TranslatorType] = None
    url: Optional[str] = None
    verified: Optional[bool] = None
    want_retweets: Optional[bool] = None
    withheld_in_countries: Optional[List[Any]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'BraggadociousLegacy':
        assert isinstance(obj, dict)
        can_dm = from_union([from_bool, from_none], obj.get("can_dm"))
        can_media_tag = from_union([from_bool, from_none], obj.get("can_media_tag"))
        created_at = from_union([from_str, from_none], obj.get("created_at"))
        default_profile = from_union([from_bool, from_none], obj.get("default_profile"))
        default_profile_image = from_union([from_bool, from_none], obj.get("default_profile_image"))
        description = from_union([from_str, from_none], obj.get("description"))
        entities = from_union([TentacledEntities.from_dict, from_none], obj.get("entities"))
        fast_followers_count = from_union([from_int, from_none], obj.get("fast_followers_count"))
        favourites_count = from_union([from_int, from_none], obj.get("favourites_count"))
        followers_count = from_union([from_int, from_none], obj.get("followers_count"))
        friends_count = from_union([from_int, from_none], obj.get("friends_count"))
        has_custom_timelines = from_union([from_bool, from_none], obj.get("has_custom_timelines"))
        is_translator = from_union([from_bool, from_none], obj.get("is_translator"))
        listed_count = from_union([from_int, from_none], obj.get("listed_count"))
        location = from_union([from_str, from_none], obj.get("location"))
        media_count = from_union([from_int, from_none], obj.get("media_count"))
        name = from_union([from_str, from_none], obj.get("name"))
        normal_followers_count = from_union([from_int, from_none], obj.get("normal_followers_count"))
        pinned_tweet_ids_str = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("pinned_tweet_ids_str"))
        possibly_sensitive = from_union([from_bool, from_none], obj.get("possibly_sensitive"))
        profile_banner_url = from_union([from_str, from_none], obj.get("profile_banner_url"))
        profile_image_url_https = from_union([from_str, from_none], obj.get("profile_image_url_https"))
        profile_interstitial_type = from_union([from_str, from_none], obj.get("profile_interstitial_type"))
        screen_name = from_union([from_str, from_none], obj.get("screen_name"))
        statuses_count = from_union([from_int, from_none], obj.get("statuses_count"))
        translator_type = from_union([TranslatorType, from_none], obj.get("translator_type"))
        url = from_union([from_str, from_none], obj.get("url"))
        verified = from_union([from_bool, from_none], obj.get("verified"))
        want_retweets = from_union([from_bool, from_none], obj.get("want_retweets"))
        withheld_in_countries = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("withheld_in_countries"))
        return BraggadociousLegacy(can_dm, can_media_tag, created_at, default_profile, default_profile_image, description, entities, fast_followers_count, favourites_count, followers_count, friends_count, has_custom_timelines, is_translator, listed_count, location, media_count, name, normal_followers_count, pinned_tweet_ids_str, possibly_sensitive, profile_banner_url, profile_image_url_https, profile_interstitial_type, screen_name, statuses_count, translator_type, url, verified, want_retweets, withheld_in_countries)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.can_dm is not None:
            result["can_dm"] = from_union([from_bool, from_none], self.can_dm)
        if self.can_media_tag is not None:
            result["can_media_tag"] = from_union([from_bool, from_none], self.can_media_tag)
        if self.created_at is not None:
            result["created_at"] = from_union([from_str, from_none], self.created_at)
        if self.default_profile is not None:
            result["default_profile"] = from_union([from_bool, from_none], self.default_profile)
        if self.default_profile_image is not None:
            result["default_profile_image"] = from_union([from_bool, from_none], self.default_profile_image)
        if self.description is not None:
            result["description"] = from_union([from_str, from_none], self.description)
        if self.entities is not None:
            result["entities"] = from_union([lambda x: to_class(TentacledEntities, x), from_none], self.entities)
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
            result["location"] = from_union([from_str, from_none], self.location)
        if self.media_count is not None:
            result["media_count"] = from_union([from_int, from_none], self.media_count)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.normal_followers_count is not None:
            result["normal_followers_count"] = from_union([from_int, from_none], self.normal_followers_count)
        if self.pinned_tweet_ids_str is not None:
            result["pinned_tweet_ids_str"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.pinned_tweet_ids_str)
        if self.possibly_sensitive is not None:
            result["possibly_sensitive"] = from_union([from_bool, from_none], self.possibly_sensitive)
        if self.profile_banner_url is not None:
            result["profile_banner_url"] = from_union([from_str, from_none], self.profile_banner_url)
        if self.profile_image_url_https is not None:
            result["profile_image_url_https"] = from_union([from_str, from_none], self.profile_image_url_https)
        if self.profile_interstitial_type is not None:
            result["profile_interstitial_type"] = from_union([from_str, from_none], self.profile_interstitial_type)
        if self.screen_name is not None:
            result["screen_name"] = from_union([from_str, from_none], self.screen_name)
        if self.statuses_count is not None:
            result["statuses_count"] = from_union([from_int, from_none], self.statuses_count)
        if self.translator_type is not None:
            result["translator_type"] = from_union([lambda x: to_enum(TranslatorType, x), from_none], self.translator_type)
        if self.url is not None:
            result["url"] = from_union([from_str, from_none], self.url)
        if self.verified is not None:
            result["verified"] = from_union([from_bool, from_none], self.verified)
        if self.want_retweets is not None:
            result["want_retweets"] = from_union([from_bool, from_none], self.want_retweets)
        if self.withheld_in_countries is not None:
            result["withheld_in_countries"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.withheld_in_countries)
        return result


@dataclass
class FriskyResult:
    typename: Optional[UserDisplayTypeEnum] = None
    id: Optional[str] = None
    rest_id: Optional[str] = None
    affiliates_highlighted_label: Optional[AffiliatesHighlightedLabel] = None
    has_graduated_access: Optional[bool] = None
    is_blue_verified: Optional[bool] = None
    profile_image_shape: Optional[ProfileImageShape] = None
    legacy: Optional[BraggadociousLegacy] = None
    smart_blocked_by: Optional[bool] = None
    smart_blocking: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'FriskyResult':
        assert isinstance(obj, dict)
        typename = from_union([UserDisplayTypeEnum, from_none], obj.get("__typename"))
        id = from_union([from_str, from_none], obj.get("id"))
        rest_id = from_union([from_str, from_none], obj.get("rest_id"))
        affiliates_highlighted_label = from_union([AffiliatesHighlightedLabel.from_dict, from_none], obj.get("affiliates_highlighted_label"))
        has_graduated_access = from_union([from_bool, from_none], obj.get("has_graduated_access"))
        is_blue_verified = from_union([from_bool, from_none], obj.get("is_blue_verified"))
        profile_image_shape = from_union([ProfileImageShape, from_none], obj.get("profile_image_shape"))
        legacy = from_union([BraggadociousLegacy.from_dict, from_none], obj.get("legacy"))
        smart_blocked_by = from_union([from_bool, from_none], obj.get("smart_blocked_by"))
        smart_blocking = from_union([from_bool, from_none], obj.get("smart_blocking"))
        return FriskyResult(typename, id, rest_id, affiliates_highlighted_label, has_graduated_access, is_blue_verified, profile_image_shape, legacy, smart_blocked_by, smart_blocking)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.typename is not None:
            result["__typename"] = from_union([lambda x: to_enum(UserDisplayTypeEnum, x), from_none], self.typename)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.rest_id is not None:
            result["rest_id"] = from_union([from_str, from_none], self.rest_id)
        if self.affiliates_highlighted_label is not None:
            result["affiliates_highlighted_label"] = from_union([lambda x: to_class(AffiliatesHighlightedLabel, x), from_none], self.affiliates_highlighted_label)
        if self.has_graduated_access is not None:
            result["has_graduated_access"] = from_union([from_bool, from_none], self.has_graduated_access)
        if self.is_blue_verified is not None:
            result["is_blue_verified"] = from_union([from_bool, from_none], self.is_blue_verified)
        if self.profile_image_shape is not None:
            result["profile_image_shape"] = from_union([lambda x: to_enum(ProfileImageShape, x), from_none], self.profile_image_shape)
        if self.legacy is not None:
            result["legacy"] = from_union([lambda x: to_class(BraggadociousLegacy, x), from_none], self.legacy)
        if self.smart_blocked_by is not None:
            result["smart_blocked_by"] = from_union([from_bool, from_none], self.smart_blocked_by)
        if self.smart_blocking is not None:
            result["smart_blocking"] = from_union([from_bool, from_none], self.smart_blocking)
        return result


@dataclass
class IndecentUserResults:
    result: Optional[FriskyResult] = None

    @staticmethod
    def from_dict(obj: Any) -> 'IndecentUserResults':
        assert isinstance(obj, dict)
        result = from_union([FriskyResult.from_dict, from_none], obj.get("result"))
        return IndecentUserResults(result)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.result is not None:
            result["result"] = from_union([lambda x: to_class(FriskyResult, x), from_none], self.result)
        return result


@dataclass
class IndecentCore:
    user_results: Optional[IndecentUserResults] = None

    @staticmethod
    def from_dict(obj: Any) -> 'IndecentCore':
        assert isinstance(obj, dict)
        user_results = from_union([IndecentUserResults.from_dict, from_none], obj.get("user_results"))
        return IndecentCore(user_results)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.user_results is not None:
            result["user_results"] = from_union([lambda x: to_class(IndecentUserResults, x), from_none], self.user_results)
        return result


@dataclass
class AmbitiousEntities:
    user_mentions: Optional[List[Any]] = None
    urls: Optional[List[Any]] = None
    hashtags: Optional[List[Hashtag]] = None
    symbols: Optional[List[Any]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AmbitiousEntities':
        assert isinstance(obj, dict)
        user_mentions = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("user_mentions"))
        urls = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("urls"))
        hashtags = from_union([lambda x: from_list(Hashtag.from_dict, x), from_none], obj.get("hashtags"))
        symbols = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("symbols"))
        return AmbitiousEntities(user_mentions, urls, hashtags, symbols)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.user_mentions is not None:
            result["user_mentions"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.user_mentions)
        if self.urls is not None:
            result["urls"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.urls)
        if self.hashtags is not None:
            result["hashtags"] = from_union([lambda x: from_list(lambda x: to_class(Hashtag, x), x), from_none], self.hashtags)
        if self.symbols is not None:
            result["symbols"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.symbols)
        return result


@dataclass
class Legacy1:
    bookmark_count: Optional[int] = None
    bookmarked: Optional[bool] = None
    created_at: Optional[str] = None
    conversation_id_str: Optional[str] = None
    display_text_range: Optional[List[int]] = None
    entities: Optional[AmbitiousEntities] = None
    favorite_count: Optional[int] = None
    favorited: Optional[bool] = None
    full_text: Optional[str] = None
    is_quote_status: Optional[bool] = None
    lang: Optional[PurpleLang] = None
    quote_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None
    retweeted: Optional[bool] = None
    user_id_str: Optional[str] = None
    id_str: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Legacy1':
        assert isinstance(obj, dict)
        bookmark_count = from_union([from_int, from_none], obj.get("bookmark_count"))
        bookmarked = from_union([from_bool, from_none], obj.get("bookmarked"))
        created_at = from_union([from_str, from_none], obj.get("created_at"))
        conversation_id_str = from_union([from_str, from_none], obj.get("conversation_id_str"))
        display_text_range = from_union([lambda x: from_list(from_int, x), from_none], obj.get("display_text_range"))
        entities = from_union([AmbitiousEntities.from_dict, from_none], obj.get("entities"))
        favorite_count = from_union([from_int, from_none], obj.get("favorite_count"))
        favorited = from_union([from_bool, from_none], obj.get("favorited"))
        full_text = from_union([from_str, from_none], obj.get("full_text"))
        is_quote_status = from_union([from_bool, from_none], obj.get("is_quote_status"))
        lang = from_union([PurpleLang, from_none], obj.get("lang"))
        quote_count = from_union([from_int, from_none], obj.get("quote_count"))
        reply_count = from_union([from_int, from_none], obj.get("reply_count"))
        retweet_count = from_union([from_int, from_none], obj.get("retweet_count"))
        retweeted = from_union([from_bool, from_none], obj.get("retweeted"))
        user_id_str = from_union([from_str, from_none], obj.get("user_id_str"))
        id_str = from_union([from_str, from_none], obj.get("id_str"))
        return Legacy1(bookmark_count, bookmarked, created_at, conversation_id_str, display_text_range, entities, favorite_count, favorited, full_text, is_quote_status, lang, quote_count, reply_count, retweet_count, retweeted, user_id_str, id_str)

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
            result["entities"] = from_union([lambda x: to_class(AmbitiousEntities, x), from_none], self.entities)
        if self.favorite_count is not None:
            result["favorite_count"] = from_union([from_int, from_none], self.favorite_count)
        if self.favorited is not None:
            result["favorited"] = from_union([from_bool, from_none], self.favorited)
        if self.full_text is not None:
            result["full_text"] = from_union([from_str, from_none], self.full_text)
        if self.is_quote_status is not None:
            result["is_quote_status"] = from_union([from_bool, from_none], self.is_quote_status)
        if self.lang is not None:
            result["lang"] = from_union([lambda x: to_enum(PurpleLang, x), from_none], self.lang)
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
        return result


@dataclass
class MagentaResult:
    typename: Optional[TweetDisplayType] = None
    rest_id: Optional[str] = None
    has_birdwatch_notes: Optional[bool] = None
    core: Optional[IndecentCore] = None
    edit_control: Optional[EditControl] = None
    edit_perspective: Optional[EditPerspective] = None
    is_translatable: Optional[bool] = None
    views: Optional[Views] = None
    source: Optional[str] = None
    legacy: Optional[Legacy1] = None

    @staticmethod
    def from_dict(obj: Any) -> 'MagentaResult':
        assert isinstance(obj, dict)
        typename = from_union([TweetDisplayType, from_none], obj.get("__typename"))
        rest_id = from_union([from_str, from_none], obj.get("rest_id"))
        has_birdwatch_notes = from_union([from_bool, from_none], obj.get("has_birdwatch_notes"))
        core = from_union([IndecentCore.from_dict, from_none], obj.get("core"))
        edit_control = from_union([EditControl.from_dict, from_none], obj.get("edit_control"))
        edit_perspective = from_union([EditPerspective.from_dict, from_none], obj.get("edit_perspective"))
        is_translatable = from_union([from_bool, from_none], obj.get("is_translatable"))
        views = from_union([Views.from_dict, from_none], obj.get("views"))
        source = from_union([from_str, from_none], obj.get("source"))
        legacy = from_union([Legacy1.from_dict, from_none], obj.get("legacy"))
        return MagentaResult(typename, rest_id, has_birdwatch_notes, core, edit_control, edit_perspective, is_translatable, views, source, legacy)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.typename is not None:
            result["__typename"] = from_union([lambda x: to_enum(TweetDisplayType, x), from_none], self.typename)
        if self.rest_id is not None:
            result["rest_id"] = from_union([from_str, from_none], self.rest_id)
        if self.has_birdwatch_notes is not None:
            result["has_birdwatch_notes"] = from_union([from_bool, from_none], self.has_birdwatch_notes)
        if self.core is not None:
            result["core"] = from_union([lambda x: to_class(IndecentCore, x), from_none], self.core)
        if self.edit_control is not None:
            result["edit_control"] = from_union([lambda x: to_class(EditControl, x), from_none], self.edit_control)
        if self.edit_perspective is not None:
            result["edit_perspective"] = from_union([lambda x: to_class(EditPerspective, x), from_none], self.edit_perspective)
        if self.is_translatable is not None:
            result["is_translatable"] = from_union([from_bool, from_none], self.is_translatable)
        if self.views is not None:
            result["views"] = from_union([lambda x: to_class(Views, x), from_none], self.views)
        if self.source is not None:
            result["source"] = from_union([from_str, from_none], self.source)
        if self.legacy is not None:
            result["legacy"] = from_union([lambda x: to_class(Legacy1, x), from_none], self.legacy)
        return result


@dataclass
class TentacledQuotedStatusResult:
    result: Optional[MagentaResult] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TentacledQuotedStatusResult':
        assert isinstance(obj, dict)
        result = from_union([MagentaResult.from_dict, from_none], obj.get("result"))
        return TentacledQuotedStatusResult(result)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.result is not None:
            result["result"] = from_union([lambda x: to_class(MagentaResult, x), from_none], self.result)
        return result


@dataclass
class AmbitiousResult:
    typename: Optional[TweetDisplayType] = None
    rest_id: Optional[str] = None
    has_birdwatch_notes: Optional[bool] = None
    core: Optional[IndigoCore] = None
    edit_control: Optional[EditControl] = None
    edit_perspective: Optional[EditPerspective] = None
    is_translatable: Optional[bool] = None
    views: Optional[Views] = None
    source: Optional[str] = None
    legacy: Optional[MischievousLegacy] = None
    quick_promote_eligibility: Optional[QuickPromoteEligibility] = None
    card: Optional[FluffyCard] = None
    unified_card: Optional[UnifiedCard] = None
    quoted_status_result: Optional[TentacledQuotedStatusResult] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AmbitiousResult':
        assert isinstance(obj, dict)
        typename = from_union([TweetDisplayType, from_none], obj.get("__typename"))
        rest_id = from_union([from_str, from_none], obj.get("rest_id"))
        has_birdwatch_notes = from_union([from_bool, from_none], obj.get("has_birdwatch_notes"))
        core = from_union([IndigoCore.from_dict, from_none], obj.get("core"))
        edit_control = from_union([EditControl.from_dict, from_none], obj.get("edit_control"))
        edit_perspective = from_union([EditPerspective.from_dict, from_none], obj.get("edit_perspective"))
        is_translatable = from_union([from_bool, from_none], obj.get("is_translatable"))
        views = from_union([Views.from_dict, from_none], obj.get("views"))
        source = from_union([from_str, from_none], obj.get("source"))
        legacy = from_union([MischievousLegacy.from_dict, from_none], obj.get("legacy"))
        quick_promote_eligibility = from_union([QuickPromoteEligibility.from_dict, from_none], obj.get("quick_promote_eligibility"))
        card = from_union([FluffyCard.from_dict, from_none], obj.get("card"))
        unified_card = from_union([UnifiedCard.from_dict, from_none], obj.get("unified_card"))
        quoted_status_result = from_union([TentacledQuotedStatusResult.from_dict, from_none], obj.get("quoted_status_result"))
        return AmbitiousResult(typename, rest_id, has_birdwatch_notes, core, edit_control, edit_perspective, is_translatable, views, source, legacy, quick_promote_eligibility, card, unified_card, quoted_status_result)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.typename is not None:
            result["__typename"] = from_union([lambda x: to_enum(TweetDisplayType, x), from_none], self.typename)
        if self.rest_id is not None:
            result["rest_id"] = from_union([from_str, from_none], self.rest_id)
        if self.has_birdwatch_notes is not None:
            result["has_birdwatch_notes"] = from_union([from_bool, from_none], self.has_birdwatch_notes)
        if self.core is not None:
            result["core"] = from_union([lambda x: to_class(IndigoCore, x), from_none], self.core)
        if self.edit_control is not None:
            result["edit_control"] = from_union([lambda x: to_class(EditControl, x), from_none], self.edit_control)
        if self.edit_perspective is not None:
            result["edit_perspective"] = from_union([lambda x: to_class(EditPerspective, x), from_none], self.edit_perspective)
        if self.is_translatable is not None:
            result["is_translatable"] = from_union([from_bool, from_none], self.is_translatable)
        if self.views is not None:
            result["views"] = from_union([lambda x: to_class(Views, x), from_none], self.views)
        if self.source is not None:
            result["source"] = from_union([from_str, from_none], self.source)
        if self.legacy is not None:
            result["legacy"] = from_union([lambda x: to_class(MischievousLegacy, x), from_none], self.legacy)
        if self.quick_promote_eligibility is not None:
            result["quick_promote_eligibility"] = from_union([lambda x: to_class(QuickPromoteEligibility, x), from_none], self.quick_promote_eligibility)
        if self.card is not None:
            result["card"] = from_union([lambda x: to_class(FluffyCard, x), from_none], self.card)
        if self.unified_card is not None:
            result["unified_card"] = from_union([lambda x: to_class(UnifiedCard, x), from_none], self.unified_card)
        if self.quoted_status_result is not None:
            result["quoted_status_result"] = from_union([lambda x: to_class(TentacledQuotedStatusResult, x), from_none], self.quoted_status_result)
        return result


@dataclass
class FluffyTweetResults:
    result: Optional[AmbitiousResult] = None

    @staticmethod
    def from_dict(obj: Any) -> 'FluffyTweetResults':
        assert isinstance(obj, dict)
        result = from_union([AmbitiousResult.from_dict, from_none], obj.get("result"))
        return FluffyTweetResults(result)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.result is not None:
            result["result"] = from_union([lambda x: to_class(AmbitiousResult, x), from_none], self.result)
        return result


@dataclass
class DescriptionURL:
    display_url: Optional[str] = None
    expanded_url: Optional[str] = None
    url: Optional[str] = None
    indices: Optional[List[int]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DescriptionURL':
        assert isinstance(obj, dict)
        display_url = from_union([from_str, from_none], obj.get("display_url"))
        expanded_url = from_union([from_str, from_none], obj.get("expanded_url"))
        url = from_union([from_str, from_none], obj.get("url"))
        indices = from_union([lambda x: from_list(from_int, x), from_none], obj.get("indices"))
        return DescriptionURL(display_url, expanded_url, url, indices)

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
class FluffyDescription:
    urls: Optional[List[DescriptionURL]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'FluffyDescription':
        assert isinstance(obj, dict)
        urls = from_union([lambda x: from_list(DescriptionURL.from_dict, x), from_none], obj.get("urls"))
        return FluffyDescription(urls)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.urls is not None:
            result["urls"] = from_union([lambda x: from_list(lambda x: to_class(DescriptionURL, x), x), from_none], self.urls)
        return result


@dataclass
class HilariousURL:
    display_url: Optional[str] = None
    expanded_url: Optional[str] = None
    url: Optional[str] = None
    indices: Optional[List[int]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'HilariousURL':
        assert isinstance(obj, dict)
        display_url = from_union([from_str, from_none], obj.get("display_url"))
        expanded_url = from_union([from_str, from_none], obj.get("expanded_url"))
        url = from_union([from_str, from_none], obj.get("url"))
        indices = from_union([lambda x: from_list(from_int, x), from_none], obj.get("indices"))
        return HilariousURL(display_url, expanded_url, url, indices)

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
class IndecentURL:
    urls: Optional[List[HilariousURL]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'IndecentURL':
        assert isinstance(obj, dict)
        urls = from_union([lambda x: from_list(HilariousURL.from_dict, x), from_none], obj.get("urls"))
        return IndecentURL(urls)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.urls is not None:
            result["urls"] = from_union([lambda x: from_list(lambda x: to_class(HilariousURL, x), x), from_none], self.urls)
        return result


@dataclass
class CunningEntities:
    description: Optional[FluffyDescription] = None
    url: Optional[IndecentURL] = None

    @staticmethod
    def from_dict(obj: Any) -> 'CunningEntities':
        assert isinstance(obj, dict)
        description = from_union([FluffyDescription.from_dict, from_none], obj.get("description"))
        url = from_union([IndecentURL.from_dict, from_none], obj.get("url"))
        return CunningEntities(description, url)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.description is not None:
            result["description"] = from_union([lambda x: to_class(FluffyDescription, x), from_none], self.description)
        if self.url is not None:
            result["url"] = from_union([lambda x: to_class(IndecentURL, x), from_none], self.url)
        return result


@dataclass
class Legacy2:
    can_dm: Optional[bool] = None
    can_media_tag: Optional[bool] = None
    created_at: Optional[str] = None
    default_profile: Optional[bool] = None
    default_profile_image: Optional[bool] = None
    description: Optional[str] = None
    entities: Optional[CunningEntities] = None
    fast_followers_count: Optional[int] = None
    favourites_count: Optional[int] = None
    followers_count: Optional[int] = None
    friends_count: Optional[int] = None
    has_custom_timelines: Optional[bool] = None
    is_translator: Optional[bool] = None
    listed_count: Optional[int] = None
    location: Optional[str] = None
    media_count: Optional[int] = None
    name: Optional[str] = None
    normal_followers_count: Optional[int] = None
    pinned_tweet_ids_str: Optional[List[Any]] = None
    possibly_sensitive: Optional[bool] = None
    profile_banner_url: Optional[str] = None
    profile_image_url_https: Optional[str] = None
    profile_interstitial_type: Optional[str] = None
    screen_name: Optional[str] = None
    statuses_count: Optional[int] = None
    translator_type: Optional[TranslatorType] = None
    url: Optional[str] = None
    verified: Optional[bool] = None
    want_retweets: Optional[bool] = None
    withheld_in_countries: Optional[List[Any]] = None
    verified_type: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Legacy2':
        assert isinstance(obj, dict)
        can_dm = from_union([from_bool, from_none], obj.get("can_dm"))
        can_media_tag = from_union([from_bool, from_none], obj.get("can_media_tag"))
        created_at = from_union([from_str, from_none], obj.get("created_at"))
        default_profile = from_union([from_bool, from_none], obj.get("default_profile"))
        default_profile_image = from_union([from_bool, from_none], obj.get("default_profile_image"))
        description = from_union([from_str, from_none], obj.get("description"))
        entities = from_union([CunningEntities.from_dict, from_none], obj.get("entities"))
        fast_followers_count = from_union([from_int, from_none], obj.get("fast_followers_count"))
        favourites_count = from_union([from_int, from_none], obj.get("favourites_count"))
        followers_count = from_union([from_int, from_none], obj.get("followers_count"))
        friends_count = from_union([from_int, from_none], obj.get("friends_count"))
        has_custom_timelines = from_union([from_bool, from_none], obj.get("has_custom_timelines"))
        is_translator = from_union([from_bool, from_none], obj.get("is_translator"))
        listed_count = from_union([from_int, from_none], obj.get("listed_count"))
        location = from_union([from_str, from_none], obj.get("location"))
        media_count = from_union([from_int, from_none], obj.get("media_count"))
        name = from_union([from_str, from_none], obj.get("name"))
        normal_followers_count = from_union([from_int, from_none], obj.get("normal_followers_count"))
        pinned_tweet_ids_str = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("pinned_tweet_ids_str"))
        possibly_sensitive = from_union([from_bool, from_none], obj.get("possibly_sensitive"))
        profile_banner_url = from_union([from_str, from_none], obj.get("profile_banner_url"))
        profile_image_url_https = from_union([from_str, from_none], obj.get("profile_image_url_https"))
        profile_interstitial_type = from_union([from_str, from_none], obj.get("profile_interstitial_type"))
        screen_name = from_union([from_str, from_none], obj.get("screen_name"))
        statuses_count = from_union([from_int, from_none], obj.get("statuses_count"))
        translator_type = from_union([TranslatorType, from_none], obj.get("translator_type"))
        url = from_union([from_str, from_none], obj.get("url"))
        verified = from_union([from_bool, from_none], obj.get("verified"))
        want_retweets = from_union([from_bool, from_none], obj.get("want_retweets"))
        withheld_in_countries = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("withheld_in_countries"))
        verified_type = from_union([from_str, from_none], obj.get("verified_type"))
        return Legacy2(can_dm, can_media_tag, created_at, default_profile, default_profile_image, description, entities, fast_followers_count, favourites_count, followers_count, friends_count, has_custom_timelines, is_translator, listed_count, location, media_count, name, normal_followers_count, pinned_tweet_ids_str, possibly_sensitive, profile_banner_url, profile_image_url_https, profile_interstitial_type, screen_name, statuses_count, translator_type, url, verified, want_retweets, withheld_in_countries, verified_type)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.can_dm is not None:
            result["can_dm"] = from_union([from_bool, from_none], self.can_dm)
        if self.can_media_tag is not None:
            result["can_media_tag"] = from_union([from_bool, from_none], self.can_media_tag)
        if self.created_at is not None:
            result["created_at"] = from_union([from_str, from_none], self.created_at)
        if self.default_profile is not None:
            result["default_profile"] = from_union([from_bool, from_none], self.default_profile)
        if self.default_profile_image is not None:
            result["default_profile_image"] = from_union([from_bool, from_none], self.default_profile_image)
        if self.description is not None:
            result["description"] = from_union([from_str, from_none], self.description)
        if self.entities is not None:
            result["entities"] = from_union([lambda x: to_class(CunningEntities, x), from_none], self.entities)
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
            result["location"] = from_union([from_str, from_none], self.location)
        if self.media_count is not None:
            result["media_count"] = from_union([from_int, from_none], self.media_count)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.normal_followers_count is not None:
            result["normal_followers_count"] = from_union([from_int, from_none], self.normal_followers_count)
        if self.pinned_tweet_ids_str is not None:
            result["pinned_tweet_ids_str"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.pinned_tweet_ids_str)
        if self.possibly_sensitive is not None:
            result["possibly_sensitive"] = from_union([from_bool, from_none], self.possibly_sensitive)
        if self.profile_banner_url is not None:
            result["profile_banner_url"] = from_union([from_str, from_none], self.profile_banner_url)
        if self.profile_image_url_https is not None:
            result["profile_image_url_https"] = from_union([from_str, from_none], self.profile_image_url_https)
        if self.profile_interstitial_type is not None:
            result["profile_interstitial_type"] = from_union([from_str, from_none], self.profile_interstitial_type)
        if self.screen_name is not None:
            result["screen_name"] = from_union([from_str, from_none], self.screen_name)
        if self.statuses_count is not None:
            result["statuses_count"] = from_union([from_int, from_none], self.statuses_count)
        if self.translator_type is not None:
            result["translator_type"] = from_union([lambda x: to_enum(TranslatorType, x), from_none], self.translator_type)
        if self.url is not None:
            result["url"] = from_union([from_str, from_none], self.url)
        if self.verified is not None:
            result["verified"] = from_union([from_bool, from_none], self.verified)
        if self.want_retweets is not None:
            result["want_retweets"] = from_union([from_bool, from_none], self.want_retweets)
        if self.withheld_in_countries is not None:
            result["withheld_in_countries"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.withheld_in_countries)
        if self.verified_type is not None:
            result["verified_type"] = from_union([from_str, from_none], self.verified_type)
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


@dataclass
class MischievousResult:
    typename: Optional[UserDisplayTypeEnum] = None
    id: Optional[str] = None
    rest_id: Optional[str] = None
    affiliates_highlighted_label: Optional[AffiliatesHighlightedLabel] = None
    has_graduated_access: Optional[bool] = None
    is_blue_verified: Optional[bool] = None
    profile_image_shape: Optional[ProfileImageShape] = None
    legacy: Optional[Legacy2] = None
    smart_blocked_by: Optional[bool] = None
    smart_blocking: Optional[bool] = None
    professional: Optional[Professional] = None

    @staticmethod
    def from_dict(obj: Any) -> 'MischievousResult':
        assert isinstance(obj, dict)
        typename = from_union([UserDisplayTypeEnum, from_none], obj.get("__typename"))
        id = from_union([from_str, from_none], obj.get("id"))
        rest_id = from_union([from_str, from_none], obj.get("rest_id"))
        affiliates_highlighted_label = from_union([AffiliatesHighlightedLabel.from_dict, from_none], obj.get("affiliates_highlighted_label"))
        has_graduated_access = from_union([from_bool, from_none], obj.get("has_graduated_access"))
        is_blue_verified = from_union([from_bool, from_none], obj.get("is_blue_verified"))
        profile_image_shape = from_union([ProfileImageShape, from_none], obj.get("profile_image_shape"))
        legacy = from_union([Legacy2.from_dict, from_none], obj.get("legacy"))
        smart_blocked_by = from_union([from_bool, from_none], obj.get("smart_blocked_by"))
        smart_blocking = from_union([from_bool, from_none], obj.get("smart_blocking"))
        professional = from_union([Professional.from_dict, from_none], obj.get("professional"))
        return MischievousResult(typename, id, rest_id, affiliates_highlighted_label, has_graduated_access, is_blue_verified, profile_image_shape, legacy, smart_blocked_by, smart_blocking, professional)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.typename is not None:
            result["__typename"] = from_union([lambda x: to_enum(UserDisplayTypeEnum, x), from_none], self.typename)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.rest_id is not None:
            result["rest_id"] = from_union([from_str, from_none], self.rest_id)
        if self.affiliates_highlighted_label is not None:
            result["affiliates_highlighted_label"] = from_union([lambda x: to_class(AffiliatesHighlightedLabel, x), from_none], self.affiliates_highlighted_label)
        if self.has_graduated_access is not None:
            result["has_graduated_access"] = from_union([from_bool, from_none], self.has_graduated_access)
        if self.is_blue_verified is not None:
            result["is_blue_verified"] = from_union([from_bool, from_none], self.is_blue_verified)
        if self.profile_image_shape is not None:
            result["profile_image_shape"] = from_union([lambda x: to_enum(ProfileImageShape, x), from_none], self.profile_image_shape)
        if self.legacy is not None:
            result["legacy"] = from_union([lambda x: to_class(Legacy2, x), from_none], self.legacy)
        if self.smart_blocked_by is not None:
            result["smart_blocked_by"] = from_union([from_bool, from_none], self.smart_blocked_by)
        if self.smart_blocking is not None:
            result["smart_blocking"] = from_union([from_bool, from_none], self.smart_blocking)
        if self.professional is not None:
            result["professional"] = from_union([lambda x: to_class(Professional, x), from_none], self.professional)
        return result


@dataclass
class ItemContentUserResults:
    result: Optional[MischievousResult] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ItemContentUserResults':
        assert isinstance(obj, dict)
        result = from_union([MischievousResult.from_dict, from_none], obj.get("result"))
        return ItemContentUserResults(result)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.result is not None:
            result["result"] = from_union([lambda x: to_class(MischievousResult, x), from_none], self.result)
        return result


@dataclass
class ItemItemContent:
    item_type: Optional[ItemTypeEnum] = None
    typename: Optional[ItemTypeEnum] = None
    tweet_results: Optional[FluffyTweetResults] = None
    tweet_display_type: Optional[TweetDisplayType] = None
    user_results: Optional[ItemContentUserResults] = None
    user_display_type: Optional[UserDisplayTypeEnum] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ItemItemContent':
        assert isinstance(obj, dict)
        item_type = from_union([ItemTypeEnum, from_none], obj.get("itemType"))
        typename = from_union([ItemTypeEnum, from_none], obj.get("__typename"))
        tweet_results = from_union([FluffyTweetResults.from_dict, from_none], obj.get("tweet_results"))
        tweet_display_type = from_union([TweetDisplayType, from_none], obj.get("tweetDisplayType"))
        user_results = from_union([ItemContentUserResults.from_dict, from_none], obj.get("user_results"))
        user_display_type = from_union([UserDisplayTypeEnum, from_none], obj.get("userDisplayType"))
        return ItemItemContent(item_type, typename, tweet_results, tweet_display_type, user_results, user_display_type)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.item_type is not None:
            result["itemType"] = from_union([lambda x: to_enum(ItemTypeEnum, x), from_none], self.item_type)
        if self.typename is not None:
            result["__typename"] = from_union([lambda x: to_enum(ItemTypeEnum, x), from_none], self.typename)
        if self.tweet_results is not None:
            result["tweet_results"] = from_union([lambda x: to_class(FluffyTweetResults, x), from_none], self.tweet_results)
        if self.tweet_display_type is not None:
            result["tweetDisplayType"] = from_union([lambda x: to_enum(TweetDisplayType, x), from_none], self.tweet_display_type)
        if self.user_results is not None:
            result["user_results"] = from_union([lambda x: to_class(ItemContentUserResults, x), from_none], self.user_results)
        if self.user_display_type is not None:
            result["userDisplayType"] = from_union([lambda x: to_enum(UserDisplayTypeEnum, x), from_none], self.user_display_type)
        return result


@dataclass
class ItemItem:
    item_content: Optional[ItemItemContent] = None
    client_event_info: Optional[ItemClientEventInfo] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ItemItem':
        assert isinstance(obj, dict)
        item_content = from_union([ItemItemContent.from_dict, from_none], obj.get("itemContent"))
        client_event_info = from_union([ItemClientEventInfo.from_dict, from_none], obj.get("clientEventInfo"))
        return ItemItem(item_content, client_event_info)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.item_content is not None:
            result["itemContent"] = from_union([lambda x: to_class(ItemItemContent, x), from_none], self.item_content)
        if self.client_event_info is not None:
            result["clientEventInfo"] = from_union([lambda x: to_class(ItemClientEventInfo, x), from_none], self.client_event_info)
        return result


@dataclass
class ItemElement:
    entry_id: Optional[str] = None
    item: Optional[ItemItem] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ItemElement':
        assert isinstance(obj, dict)
        entry_id = from_union([from_str, from_none], obj.get("entryId"))
        item = from_union([ItemItem.from_dict, from_none], obj.get("item"))
        return ItemElement(entry_id, item)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.entry_id is not None:
            result["entryId"] = from_union([from_str, from_none], self.entry_id)
        if self.item is not None:
            result["item"] = from_union([lambda x: to_class(ItemItem, x), from_none], self.item)
        return result


@dataclass
class ConversationMetadata:
    all_tweet_ids: Optional[List[str]] = None
    enable_deduplication: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ConversationMetadata':
        assert isinstance(obj, dict)
        all_tweet_ids = from_union([lambda x: from_list(from_str, x), from_none], obj.get("allTweetIds"))
        enable_deduplication = from_union([from_bool, from_none], obj.get("enableDeduplication"))
        return ConversationMetadata(all_tweet_ids, enable_deduplication)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.all_tweet_ids is not None:
            result["allTweetIds"] = from_union([lambda x: from_list(from_str, x), from_none], self.all_tweet_ids)
        if self.enable_deduplication is not None:
            result["enableDeduplication"] = from_union([from_bool, from_none], self.enable_deduplication)
        return result


@dataclass
class ContentMetadata:
    conversation_metadata: Optional[ConversationMetadata] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ContentMetadata':
        assert isinstance(obj, dict)
        conversation_metadata = from_union([ConversationMetadata.from_dict, from_none], obj.get("conversationMetadata"))
        return ContentMetadata(conversation_metadata)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.conversation_metadata is not None:
            result["conversationMetadata"] = from_union([lambda x: to_class(ConversationMetadata, x), from_none], self.conversation_metadata)
        return result


@dataclass
class Content:
    entry_type: Optional[EntryTypeEnum] = None
    typename: Optional[EntryTypeEnum] = None
    item_content: Optional[ContentItemContent] = None
    client_event_info: Optional[ContentClientEventInfo] = None
    items: Optional[List[ItemElement]] = None
    metadata: Optional[ContentMetadata] = None
    display_type: Optional[DisplayType] = None
    header: Optional[Header] = None
    footer: Optional[Footer] = None
    value: Optional[str] = None
    cursor_type: Optional[CursorType] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Content':
        assert isinstance(obj, dict)
        entry_type = from_union([EntryTypeEnum, from_none], obj.get("entryType"))
        typename = from_union([EntryTypeEnum, from_none], obj.get("__typename"))
        item_content = from_union([ContentItemContent.from_dict, from_none], obj.get("itemContent"))
        client_event_info = from_union([ContentClientEventInfo.from_dict, from_none], obj.get("clientEventInfo"))
        items = from_union([lambda x: from_list(ItemElement.from_dict, x), from_none], obj.get("items"))
        metadata = from_union([ContentMetadata.from_dict, from_none], obj.get("metadata"))
        display_type = from_union([DisplayType, from_none], obj.get("displayType"))
        header = from_union([Header.from_dict, from_none], obj.get("header"))
        footer = from_union([Footer.from_dict, from_none], obj.get("footer"))
        value = from_union([from_str, from_none], obj.get("value"))
        cursor_type = from_union([CursorType, from_none], obj.get("cursorType"))
        return Content(entry_type, typename, item_content, client_event_info, items, metadata, display_type, header, footer, value, cursor_type)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.entry_type is not None:
            result["entryType"] = from_union([lambda x: to_enum(EntryTypeEnum, x), from_none], self.entry_type)
        if self.typename is not None:
            result["__typename"] = from_union([lambda x: to_enum(EntryTypeEnum, x), from_none], self.typename)
        if self.item_content is not None:
            result["itemContent"] = from_union([lambda x: to_class(ContentItemContent, x), from_none], self.item_content)
        if self.client_event_info is not None:
            result["clientEventInfo"] = from_union([lambda x: to_class(ContentClientEventInfo, x), from_none], self.client_event_info)
        if self.items is not None:
            result["items"] = from_union([lambda x: from_list(lambda x: to_class(ItemElement, x), x), from_none], self.items)
        if self.metadata is not None:
            result["metadata"] = from_union([lambda x: to_class(ContentMetadata, x), from_none], self.metadata)
        if self.display_type is not None:
            result["displayType"] = from_union([lambda x: to_enum(DisplayType, x), from_none], self.display_type)
        if self.header is not None:
            result["header"] = from_union([lambda x: to_class(Header, x), from_none], self.header)
        if self.footer is not None:
            result["footer"] = from_union([lambda x: to_class(Footer, x), from_none], self.footer)
        if self.value is not None:
            result["value"] = from_union([from_str, from_none], self.value)
        if self.cursor_type is not None:
            result["cursorType"] = from_union([lambda x: to_enum(CursorType, x), from_none], self.cursor_type)
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


class Page(Enum):
    PROFILE_BEST = "profileBest"


@dataclass
class ScribeConfig:
    page: Optional[Page] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ScribeConfig':
        assert isinstance(obj, dict)
        page = from_union([Page, from_none], obj.get("page"))
        return ScribeConfig(page)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.page is not None:
            result["page"] = from_union([lambda x: to_enum(Page, x), from_none], self.page)
        return result


@dataclass
class TimelineMetadata:
    scribe_config: Optional[ScribeConfig] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TimelineMetadata':
        assert isinstance(obj, dict)
        scribe_config = from_union([ScribeConfig.from_dict, from_none], obj.get("scribeConfig"))
        return TimelineMetadata(scribe_config)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.scribe_config is not None:
            result["scribeConfig"] = from_union([lambda x: to_class(ScribeConfig, x), from_none], self.scribe_config)
        return result


@dataclass
class Timeline:
    instructions: Optional[List[Instruction]] = None
    metadata: Optional[TimelineMetadata] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Timeline':
        assert isinstance(obj, dict)
        instructions = from_union([lambda x: from_list(Instruction.from_dict, x), from_none], obj.get("instructions"))
        metadata = from_union([TimelineMetadata.from_dict, from_none], obj.get("metadata"))
        return Timeline(instructions, metadata)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.instructions is not None:
            result["instructions"] = from_union([lambda x: from_list(lambda x: to_class(Instruction, x), x), from_none], self.instructions)
        if self.metadata is not None:
            result["metadata"] = from_union([lambda x: to_class(TimelineMetadata, x), from_none], self.metadata)
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
    typename: Optional[UserDisplayTypeEnum] = None
    timeline_v2: Optional[TimelineV2] = None

    @staticmethod
    def from_dict(obj: Any) -> 'UserResult':
        assert isinstance(obj, dict)
        typename = from_union([UserDisplayTypeEnum, from_none], obj.get("__typename"))
        timeline_v2 = from_union([TimelineV2.from_dict, from_none], obj.get("timeline_v2"))
        return UserResult(typename, timeline_v2)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.typename is not None:
            result["__typename"] = from_union([lambda x: to_enum(UserDisplayTypeEnum, x), from_none], self.typename)
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


def twitter_data_from_dict(s: Any) -> List[TwitterDatum]:
    return from_list(TwitterDatum.from_dict, s)


def twitter_data_to_dict(x: List[TwitterDatum]) -> Any:
    return from_list(lambda x: to_class(TwitterDatum, x), x)
