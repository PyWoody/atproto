##################################################################
# THIS IS THE AUTO-GENERATED CODE. DON'T EDIT IT BY HANDS!
# Copyright (C) 2024 Ilya (Marshal) <https://github.com/MarshalX>.
# This file is part of Python atproto SDK. Licenced under MIT.
##################################################################


import typing as t

import typing_extensions as te
from pydantic import Field

if t.TYPE_CHECKING:
    from atproto_client import models
from atproto_client.models import base


class Params(base.ParamsModelBase):
    """Parameters model for :obj:`app.bsky.feed.searchPosts`."""

    q: str  #: Search query string; syntax, phrase, boolean, and faceting is unspecified, but Lucene query syntax is recommended.
    author: t.Optional[str] = (
        None  #: Filter to posts by the given account. Handles are resolved to DID before query-time.
    )
    cursor: t.Optional[str] = (
        None  #: Optional pagination mechanism; may not necessarily allow scrolling through entire result set.
    )
    domain: t.Optional[str] = (
        None  #: Filter to posts with URLs (facet links or embeds) linking to the given domain (hostname). Server may apply hostname normalization.
    )
    lang: t.Optional[str] = (
        None  #: Filter to posts in the given language. Expected to be based on post language field, though server may override language detection.
    )
    limit: t.Optional[int] = Field(default=25, ge=1, le=100)  #: Limit.
    mentions: t.Optional[str] = (
        None  #: Filter to posts which mention the given account. Handles are resolved to DID before query-time. Only matches rich-text facet mentions.
    )
    since: t.Optional[str] = (
        None  #: Filter results for posts after the indicated datetime (inclusive). Expected to use 'sortAt' timestamp, which may not match 'createdAt'. Can be a datetime, or just an ISO date (YYYY-MM-DD).
    )
    sort: t.Optional[t.Union[t.Literal['top'], t.Literal['latest'], str]] = (
        'latest'  #: Specifies the ranking order of results.
    )
    tag: t.Optional[t.List[str]] = (
        None  #: Filter to posts with the given tag (hashtag), based on rich-text facet or tag field. Do not include the hash (#) prefix. Multiple tags can be specified, with 'AND' matching.
    )
    until: t.Optional[str] = (
        None  #: Filter results for posts before the indicated datetime (not inclusive). Expected to use 'sortAt' timestamp, which may not match 'createdAt'. Can be a datetime, or just an ISO date (YYY-MM-DD).
    )
    url: t.Optional[str] = (
        None  #: Filter to posts with links (facet links or embeds) pointing to this URL. Server may apply URL normalization or fuzzy matching.
    )


class ParamsDict(t.TypedDict):
    q: str  #: Search query string; syntax, phrase, boolean, and faceting is unspecified, but Lucene query syntax is recommended.
    author: te.NotRequired[
        t.Optional[str]
    ]  #: Filter to posts by the given account. Handles are resolved to DID before query-time.
    cursor: te.NotRequired[
        t.Optional[str]
    ]  #: Optional pagination mechanism; may not necessarily allow scrolling through entire result set.
    domain: te.NotRequired[
        t.Optional[str]
    ]  #: Filter to posts with URLs (facet links or embeds) linking to the given domain (hostname). Server may apply hostname normalization.
    lang: te.NotRequired[
        t.Optional[str]
    ]  #: Filter to posts in the given language. Expected to be based on post language field, though server may override language detection.
    limit: te.NotRequired[t.Optional[int]]  #: Limit.
    mentions: te.NotRequired[
        t.Optional[str]
    ]  #: Filter to posts which mention the given account. Handles are resolved to DID before query-time. Only matches rich-text facet mentions.
    since: te.NotRequired[
        t.Optional[str]
    ]  #: Filter results for posts after the indicated datetime (inclusive). Expected to use 'sortAt' timestamp, which may not match 'createdAt'. Can be a datetime, or just an ISO date (YYYY-MM-DD).
    sort: te.NotRequired[
        t.Optional[t.Union[t.Literal['top'], t.Literal['latest'], str]]
    ]  #: Specifies the ranking order of results.
    tag: te.NotRequired[
        t.Optional[t.List[str]]
    ]  #: Filter to posts with the given tag (hashtag), based on rich-text facet or tag field. Do not include the hash (#) prefix. Multiple tags can be specified, with 'AND' matching.
    until: te.NotRequired[
        t.Optional[str]
    ]  #: Filter results for posts before the indicated datetime (not inclusive). Expected to use 'sortAt' timestamp, which may not match 'createdAt'. Can be a datetime, or just an ISO date (YYY-MM-DD).
    url: te.NotRequired[
        t.Optional[str]
    ]  #: Filter to posts with links (facet links or embeds) pointing to this URL. Server may apply URL normalization or fuzzy matching.


class Response(base.ResponseModelBase):
    """Output data model for :obj:`app.bsky.feed.searchPosts`."""

    posts: t.List['models.AppBskyFeedDefs.PostView']  #: Posts.
    cursor: t.Optional[str] = None  #: Cursor.
    hits_total: t.Optional[int] = (
        None  #: Count of search hits. Optional, may be rounded/truncated, and may not be possible to paginate through all hits.
    )
