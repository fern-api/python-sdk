# This file was auto-generated by Fern from our API Definition.

from .types import (
    ApiAuth,
    ApiAuth_BasicAuth,
    ApiAuth_BearerAuth,
    ApiAuth_Header,
    ApiDefinition,
    ApiDefinitionPackage,
    ApiDefinitionSubpackage,
    BasicAuth,
    BearerAuth,
    HeaderAuth,
    SubpackageId,
)
from .errors import ApiDoesNotExistError
from .resources import (
    Availability,
    CodeExamples,
    DiscriminatedUnionType,
    DiscriminatedUnionVariant,
    EndpointDefinition,
    EndpointId,
    EndpointPath,
    EndpointPathPart,
    EndpointPathPart_Literal,
    EndpointPathPart_PathParameter,
    EnumType,
    EnumValue,
    Environment,
    EnvironmentId,
    ErrorDeclaration,
    ErrorDeclarationV2,
    ExampleEndpointCall,
    ExampleEndpointRequest,
    ExampleEndpointResponse,
    ExampleWebhookPayload,
    FormValue,
    FormValue_Filename,
    FormValue_Json,
    Header,
    HttpMethod,
    HttpRequest,
    HttpRequestBodyShape,
    HttpRequestBodyShape_FileUpload,
    HttpRequestBodyShape_Object,
    HttpRequestBodyShape_Reference,
    HttpResponse,
    HttpResponseBodyShape,
    HttpResponseBodyShape_FileDownload,
    HttpResponseBodyShape_Object,
    HttpResponseBodyShape_Reference,
    HttpResponseBodyShape_StreamingText,
    ListType,
    LiteralType,
    LiteralType_StringLiteral,
    MapType,
    ObjectProperty,
    ObjectType,
    OptionalType,
    PathParameter,
    PathParameterKey,
    PrimitiveType,
    PrimitiveType_Base64,
    PrimitiveType_Boolean,
    PrimitiveType_Date,
    PrimitiveType_Datetime,
    PrimitiveType_Double,
    PrimitiveType_Integer,
    PrimitiveType_Long,
    PrimitiveType_String,
    PrimitiveType_Uuid,
    QueryParameter,
    SetType,
    TypeDefinition,
    TypeId,
    TypeReference,
    TypeReference_Id,
    TypeReference_List,
    TypeReference_Literal,
    TypeReference_Map,
    TypeReference_Optional,
    TypeReference_Primitive,
    TypeReference_Set,
    TypeReference_Unknown,
    TypeShape,
    TypeShape_Alias,
    TypeShape_DiscriminatedUnion,
    TypeShape_Enum,
    TypeShape_Object,
    TypeShape_UndiscriminatedUnion,
    UndiscriminatedUnionType,
    UndiscriminatedUnionVariant,
    WebhookDefinition,
    WebhookHttpMethod,
    WebhookId,
    WebhookPayload,
    WebhookPayloadShape,
    WebhookPayloadShape_Object,
    WebhookPayloadShape_Reference,
    WithDescription,
    commons,
    endpoint,
    type,
    webhook,
)

__all__ = [
    "ApiAuth",
    "ApiAuth_BasicAuth",
    "ApiAuth_BearerAuth",
    "ApiAuth_Header",
    "ApiDefinition",
    "ApiDefinitionPackage",
    "ApiDefinitionSubpackage",
    "ApiDoesNotExistError",
    "Availability",
    "BasicAuth",
    "BearerAuth",
    "CodeExamples",
    "DiscriminatedUnionType",
    "DiscriminatedUnionVariant",
    "EndpointDefinition",
    "EndpointId",
    "EndpointPath",
    "EndpointPathPart",
    "EndpointPathPart_Literal",
    "EndpointPathPart_PathParameter",
    "EnumType",
    "EnumValue",
    "Environment",
    "EnvironmentId",
    "ErrorDeclaration",
    "ErrorDeclarationV2",
    "ExampleEndpointCall",
    "ExampleEndpointRequest",
    "ExampleEndpointResponse",
    "ExampleWebhookPayload",
    "FormValue",
    "FormValue_Filename",
    "FormValue_Json",
    "Header",
    "HeaderAuth",
    "HttpMethod",
    "HttpRequest",
    "HttpRequestBodyShape",
    "HttpRequestBodyShape_FileUpload",
    "HttpRequestBodyShape_Object",
    "HttpRequestBodyShape_Reference",
    "HttpResponse",
    "HttpResponseBodyShape",
    "HttpResponseBodyShape_FileDownload",
    "HttpResponseBodyShape_Object",
    "HttpResponseBodyShape_Reference",
    "HttpResponseBodyShape_StreamingText",
    "ListType",
    "LiteralType",
    "LiteralType_StringLiteral",
    "MapType",
    "ObjectProperty",
    "ObjectType",
    "OptionalType",
    "PathParameter",
    "PathParameterKey",
    "PrimitiveType",
    "PrimitiveType_Base64",
    "PrimitiveType_Boolean",
    "PrimitiveType_Date",
    "PrimitiveType_Datetime",
    "PrimitiveType_Double",
    "PrimitiveType_Integer",
    "PrimitiveType_Long",
    "PrimitiveType_String",
    "PrimitiveType_Uuid",
    "QueryParameter",
    "SetType",
    "SubpackageId",
    "TypeDefinition",
    "TypeId",
    "TypeReference",
    "TypeReference_Id",
    "TypeReference_List",
    "TypeReference_Literal",
    "TypeReference_Map",
    "TypeReference_Optional",
    "TypeReference_Primitive",
    "TypeReference_Set",
    "TypeReference_Unknown",
    "TypeShape",
    "TypeShape_Alias",
    "TypeShape_DiscriminatedUnion",
    "TypeShape_Enum",
    "TypeShape_Object",
    "TypeShape_UndiscriminatedUnion",
    "UndiscriminatedUnionType",
    "UndiscriminatedUnionVariant",
    "WebhookDefinition",
    "WebhookHttpMethod",
    "WebhookId",
    "WebhookPayload",
    "WebhookPayloadShape",
    "WebhookPayloadShape_Object",
    "WebhookPayloadShape_Reference",
    "WithDescription",
    "commons",
    "endpoint",
    "type",
    "webhook",
]