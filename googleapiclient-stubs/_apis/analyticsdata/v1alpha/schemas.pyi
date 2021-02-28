import typing

import typing_extensions
@typing.type_check_only
class BatchRunPivotReportsRequest(typing_extensions.TypedDict, total=False):
    entity: Entity
    requests: typing.List[RunPivotReportRequest]

@typing.type_check_only
class BatchRunPivotReportsResponse(typing_extensions.TypedDict, total=False):
    pivotReports: typing.List[RunPivotReportResponse]

@typing.type_check_only
class BatchRunReportsRequest(typing_extensions.TypedDict, total=False):
    entity: Entity
    requests: typing.List[RunReportRequest]

@typing.type_check_only
class BatchRunReportsResponse(typing_extensions.TypedDict, total=False):
    reports: typing.List[RunReportResponse]

@typing.type_check_only
class BetweenFilter(typing_extensions.TypedDict, total=False):
    fromValue: NumericValue
    toValue: NumericValue

@typing.type_check_only
class CaseExpression(typing_extensions.TypedDict, total=False):
    dimensionName: str

@typing.type_check_only
class Cohort(typing_extensions.TypedDict, total=False):
    dateRange: DateRange
    dimension: str
    name: str

@typing.type_check_only
class CohortReportSettings(typing_extensions.TypedDict, total=False):
    accumulate: bool

@typing.type_check_only
class CohortSpec(typing_extensions.TypedDict, total=False):
    cohortReportSettings: CohortReportSettings
    cohorts: typing.List[Cohort]
    cohortsRange: CohortsRange

@typing.type_check_only
class CohortsRange(typing_extensions.TypedDict, total=False):
    endOffset: int
    granularity: typing_extensions.Literal[
        "GRANULARITY_UNSPECIFIED", "DAILY", "WEEKLY", "MONTHLY"
    ]
    startOffset: int

@typing.type_check_only
class ConcatenateExpression(typing_extensions.TypedDict, total=False):
    delimiter: str
    dimensionNames: typing.List[str]

@typing.type_check_only
class DateRange(typing_extensions.TypedDict, total=False):
    endDate: str
    name: str
    startDate: str

@typing.type_check_only
class Dimension(typing_extensions.TypedDict, total=False):
    dimensionExpression: DimensionExpression
    name: str

@typing.type_check_only
class DimensionExpression(typing_extensions.TypedDict, total=False):
    concatenate: ConcatenateExpression
    lowerCase: CaseExpression
    upperCase: CaseExpression

@typing.type_check_only
class DimensionHeader(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class DimensionMetadata(typing_extensions.TypedDict, total=False):
    apiName: str
    customDefinition: bool
    deprecatedApiNames: typing.List[str]
    description: str
    uiName: str

@typing.type_check_only
class DimensionOrderBy(typing_extensions.TypedDict, total=False):
    dimensionName: str
    orderType: typing_extensions.Literal[
        "ORDER_TYPE_UNSPECIFIED",
        "ALPHANUMERIC",
        "CASE_INSENSITIVE_ALPHANUMERIC",
        "NUMERIC",
    ]

@typing.type_check_only
class DimensionValue(typing_extensions.TypedDict, total=False):
    value: str

@typing.type_check_only
class Entity(typing_extensions.TypedDict, total=False):
    propertyId: str

@typing.type_check_only
class Filter(typing_extensions.TypedDict, total=False):
    betweenFilter: BetweenFilter
    fieldName: str
    inListFilter: InListFilter
    numericFilter: NumericFilter
    stringFilter: StringFilter

@typing.type_check_only
class FilterExpression(typing_extensions.TypedDict, total=False):
    andGroup: FilterExpressionList
    filter: Filter
    notExpression: FilterExpression
    orGroup: FilterExpressionList

@typing.type_check_only
class FilterExpressionList(typing_extensions.TypedDict, total=False):
    expressions: typing.List[FilterExpression]

@typing.type_check_only
class InListFilter(typing_extensions.TypedDict, total=False):
    caseSensitive: bool
    values: typing.List[str]

@typing.type_check_only
class Metadata(typing_extensions.TypedDict, total=False):
    dimensions: typing.List[DimensionMetadata]
    metrics: typing.List[MetricMetadata]
    name: str

@typing.type_check_only
class Metric(typing_extensions.TypedDict, total=False):
    expression: str
    invisible: bool
    name: str

@typing.type_check_only
class MetricHeader(typing_extensions.TypedDict, total=False):
    name: str
    type: typing_extensions.Literal[
        "METRIC_TYPE_UNSPECIFIED",
        "TYPE_INTEGER",
        "TYPE_FLOAT",
        "TYPE_SECONDS",
        "TYPE_MILLISECONDS",
        "TYPE_MINUTES",
        "TYPE_HOURS",
        "TYPE_STANDARD",
        "TYPE_CURRENCY",
        "TYPE_FEET",
        "TYPE_MILES",
        "TYPE_METERS",
        "TYPE_KILOMETERS",
    ]

@typing.type_check_only
class MetricMetadata(typing_extensions.TypedDict, total=False):
    apiName: str
    customDefinition: bool
    deprecatedApiNames: typing.List[str]
    description: str
    expression: str
    type: typing_extensions.Literal[
        "METRIC_TYPE_UNSPECIFIED",
        "TYPE_INTEGER",
        "TYPE_FLOAT",
        "TYPE_SECONDS",
        "TYPE_MILLISECONDS",
        "TYPE_MINUTES",
        "TYPE_HOURS",
        "TYPE_STANDARD",
        "TYPE_CURRENCY",
        "TYPE_FEET",
        "TYPE_MILES",
        "TYPE_METERS",
        "TYPE_KILOMETERS",
    ]
    uiName: str

@typing.type_check_only
class MetricOrderBy(typing_extensions.TypedDict, total=False):
    metricName: str

@typing.type_check_only
class MetricValue(typing_extensions.TypedDict, total=False):
    value: str

@typing.type_check_only
class NumericFilter(typing_extensions.TypedDict, total=False):
    operation: typing_extensions.Literal[
        "OPERATION_UNSPECIFIED",
        "EQUAL",
        "LESS_THAN",
        "LESS_THAN_OR_EQUAL",
        "GREATER_THAN",
        "GREATER_THAN_OR_EQUAL",
    ]
    value: NumericValue

@typing.type_check_only
class NumericValue(typing_extensions.TypedDict, total=False):
    doubleValue: float
    int64Value: str

@typing.type_check_only
class OrderBy(typing_extensions.TypedDict, total=False):
    desc: bool
    dimension: DimensionOrderBy
    metric: MetricOrderBy
    pivot: PivotOrderBy

@typing.type_check_only
class Pivot(typing_extensions.TypedDict, total=False):
    fieldNames: typing.List[str]
    limit: str
    metricAggregations: typing.List[str]
    offset: str
    orderBys: typing.List[OrderBy]

@typing.type_check_only
class PivotDimensionHeader(typing_extensions.TypedDict, total=False):
    dimensionValues: typing.List[DimensionValue]

@typing.type_check_only
class PivotHeader(typing_extensions.TypedDict, total=False):
    pivotDimensionHeaders: typing.List[PivotDimensionHeader]
    rowCount: int

@typing.type_check_only
class PivotOrderBy(typing_extensions.TypedDict, total=False):
    metricName: str
    pivotSelections: typing.List[PivotSelection]

@typing.type_check_only
class PivotSelection(typing_extensions.TypedDict, total=False):
    dimensionName: str
    dimensionValue: str

@typing.type_check_only
class PropertyQuota(typing_extensions.TypedDict, total=False):
    concurrentRequests: QuotaStatus
    serverErrorsPerProjectPerHour: QuotaStatus
    tokensPerDay: QuotaStatus
    tokensPerHour: QuotaStatus

@typing.type_check_only
class QuotaStatus(typing_extensions.TypedDict, total=False):
    consumed: int
    remaining: int

@typing.type_check_only
class ResponseMetaData(typing_extensions.TypedDict, total=False):
    dataLossFromOtherRow: bool

@typing.type_check_only
class Row(typing_extensions.TypedDict, total=False):
    dimensionValues: typing.List[DimensionValue]
    metricValues: typing.List[MetricValue]

@typing.type_check_only
class RunPivotReportRequest(typing_extensions.TypedDict, total=False):
    cohortSpec: CohortSpec
    currencyCode: str
    dateRanges: typing.List[DateRange]
    dimensionFilter: FilterExpression
    dimensions: typing.List[Dimension]
    entity: Entity
    keepEmptyRows: bool
    metricFilter: FilterExpression
    metrics: typing.List[Metric]
    pivots: typing.List[Pivot]
    returnPropertyQuota: bool

@typing.type_check_only
class RunPivotReportResponse(typing_extensions.TypedDict, total=False):
    aggregates: typing.List[Row]
    dimensionHeaders: typing.List[DimensionHeader]
    metadata: ResponseMetaData
    metricHeaders: typing.List[MetricHeader]
    pivotHeaders: typing.List[PivotHeader]
    propertyQuota: PropertyQuota
    rows: typing.List[Row]

@typing.type_check_only
class RunRealtimeReportRequest(typing_extensions.TypedDict, total=False):
    dimensionFilter: FilterExpression
    dimensions: typing.List[Dimension]
    limit: str
    metricAggregations: typing.List[str]
    metricFilter: FilterExpression
    metrics: typing.List[Metric]
    orderBys: typing.List[OrderBy]
    returnPropertyQuota: bool

@typing.type_check_only
class RunRealtimeReportResponse(typing_extensions.TypedDict, total=False):
    dimensionHeaders: typing.List[DimensionHeader]
    maximums: typing.List[Row]
    metricHeaders: typing.List[MetricHeader]
    minimums: typing.List[Row]
    propertyQuota: PropertyQuota
    rowCount: int
    rows: typing.List[Row]
    totals: typing.List[Row]

@typing.type_check_only
class RunReportRequest(typing_extensions.TypedDict, total=False):
    cohortSpec: CohortSpec
    currencyCode: str
    dateRanges: typing.List[DateRange]
    dimensionFilter: FilterExpression
    dimensions: typing.List[Dimension]
    entity: Entity
    keepEmptyRows: bool
    limit: str
    metricAggregations: typing.List[str]
    metricFilter: FilterExpression
    metrics: typing.List[Metric]
    offset: str
    orderBys: typing.List[OrderBy]
    returnPropertyQuota: bool

@typing.type_check_only
class RunReportResponse(typing_extensions.TypedDict, total=False):
    dimensionHeaders: typing.List[DimensionHeader]
    maximums: typing.List[Row]
    metadata: ResponseMetaData
    metricHeaders: typing.List[MetricHeader]
    minimums: typing.List[Row]
    propertyQuota: PropertyQuota
    rowCount: int
    rows: typing.List[Row]
    totals: typing.List[Row]

@typing.type_check_only
class StringFilter(typing_extensions.TypedDict, total=False):
    caseSensitive: bool
    matchType: typing_extensions.Literal[
        "MATCH_TYPE_UNSPECIFIED",
        "EXACT",
        "BEGINS_WITH",
        "ENDS_WITH",
        "CONTAINS",
        "FULL_REGEXP",
        "PARTIAL_REGEXP",
    ]
    value: str
