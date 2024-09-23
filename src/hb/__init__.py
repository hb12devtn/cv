from typing import Literal

import pydantic
import pydantic_extra_types.color as pydantic_color

from rendercv.themes.common_options import (
    EntryAreaMargins,
    LaTeXDimension,
    Margins,
    ThemeOptions,
)


class EntryAreaMarginsForClassic(EntryAreaMargins):
    """This class is a data model for the entry area margins."""

    education_degree_width: LaTeXDimension = pydantic.Field(
        default="1 cm",
        title="Date and Location Column Width",
        description=(
            "The width of the degree column in EducationEntry. The default value is"
            " 1 cm."
        ),
    )


class ProjectsAreaMarginsForClassic(pydantic.BaseModel):
    """This class is a data model for the project area margins."""

    top: LaTeXDimension = pydantic.Field(
        default="0.10 cm",
        title="Top Margin",
        description="The top margin of highlights areas. The default value is 0.10 cm.",
    )
    left: LaTeXDimension = pydantic.Field(
        default="0.4 cm",
        title="Left Margin",
        description="The left margin of highlights areas. The default value is 0.4 cm.",
    )
    vertical_between_projects: LaTeXDimension = pydantic.Field(
        default="0.10 cm",
        title="Vertical Margin Between Projects",
        description=(
            "The vertical margin between projects. The default value is 0.10 cm."
        ),
    )


class MarginsForClassic(Margins):
    """This class is a data model for the margins."""

    entry_area: EntryAreaMarginsForClassic = pydantic.Field(
        default=EntryAreaMarginsForClassic(),
        title="Entry Area Margins",
        description="Entry area margins.",
    )

    projects_area: ProjectsAreaMarginsForClassic = pydantic.Field(
        default=ProjectsAreaMarginsForClassic(),
        title="Projects Area Margins",
        description="Projects area margins.",
    )


class HbThemeOptions(ThemeOptions):
    """This class is the data model of the theme options for the `classic` theme."""

    theme: Literal["hb"]
    font: Literal[
        "Latin Modern Serif",
        "Latin Modern Sans Serif",
        "Latin Modern Mono",
        "Source Sans 3",
        "Charter",
    ] = pydantic.Field(
        default="Source Sans 3",
        title="Font",
        description="The font family of the CV. The default value is Source Sans 3.",
    )
    primary_color: pydantic_color.Color = pydantic.Field(
        default="rgb(0,79,144)",
        validate_default=True,
        title="Primary Color",
        description=(
            "The primary color of the theme. \nThe color can be specified either with"
            " their name (https://www.w3.org/TR/SVG11/types.html#ColorKeywords),"
            " hexadecimal value, RGB value, or HSL value. The default value is"
            " rgb(0,79,144)."
        ),
        examples=["Black", "7fffd4", "rgb(0,79,144)", "hsl(270, 60%, 70%)"],
    )
    secondary_color: pydantic_color.Color = pydantic.Field(
        default="rgb(0,79,144)",
        validate_default=True,
        title="Secondary Color",
        description=(
            "The secondary color of the theme. \nThe color can be specified either with"
            " their name (https://www.w3.org/TR/SVG11/types.html#ColorKeywords),"
            " hexadecimal value, RGB value, or HSL value. The default value is"
            " rgb(0,79,144)."
        ),
        examples=["Black", "7fffd4", "rgb(0,79,144)", "hsl(270, 60%, 70%)"],
    )
    tertiary_color: pydantic_color.Color = pydantic.Field(
        default="rgb(0,79,144)",
        validate_default=True,
        title="Tertiary Color",
        description=(
            "The tertiary color of the theme. \nThe color can be specified either with"
            " their name (https://www.w3.org/TR/SVG11/types.html#ColorKeywords),"
            " hexadecimal value, RGB value, or HSL value. The default value is"
            " rgb(0,79,144)."
        ),
        examples=["Black", "7fffd4", "rgb(0,79,144)", "hsl(270, 60%, 70%)"],
    )
    show_timespan_in: list[str] = pydantic.Field(
        default=[],
        title="Show Time Span in These Sections",
        description=(
            "The time span will be shown in the date and location column in these"
            " sections. The input should be a list of section titles as strings"
            " (case-sensitive). The default value is [] (no section will show the time"
            " span)."
        ),
    )
    margins: MarginsForClassic = pydantic.Field(
        default=MarginsForClassic(),
        title="Margins",
        description="Page, section title, entry field, and highlights field margins.",
    )
