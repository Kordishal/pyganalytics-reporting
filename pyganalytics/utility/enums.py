from enum import Enum


class MetricType(Enum):
    """
    The metric types.

        Time metric in HH:MM:SS format.
    """
    METRIC_TYPE_UNSPECIFIED = 'METRIC_TYPE_UNSPECIFIED'
    INTEGER = 'INTEGER'
    FLOAT = 'FLOAT'
    CURRENCY = 'CURRENCY'
    PERCENT = 'PERCENT'
    TIME = 'TIME'


class Sampling(Enum):
    """
    Values for the sampling level.
    """
    DEFAULT = 'DEFAULT'
    SMALL = 'SMALL'
    LARGE = 'LARGE'


class FilterLogicalOperator(Enum):
    """
    How the filters are logically combined.
    """
    OR = 'OR'
    AND = 'AND'


class DimensionFilterOperator(Enum):
    """
    """
    REGEXP = 'REGEXP'
    BEGINS_WITH = 'BEGINS_WITH'
    ENDS_WITH = 'ENDS_WITH'
    PARTIAL = 'PARTIAL'
    EXACT = 'EXACT'
    NUMERIC_EQUAL = 'NUMERIC_EQUAL'
    NUMERIC_GREATER_THAN = 'NUMERIC_GREATER_THAN'
    NUMERIC_LESS_THAN = 'NUMERIC_LESS_THAN'
    IN_LIST = 'IN_LIST'


class SegmentDimensionFilterOperator(Enum):
    """
    """
    REGEXP = 'REGEXP'
    BEGINS_WITH = 'BEGINS_WITH'
    ENDS_WITH = 'ENDS_WITH'
    PARTIAL = 'PARTIAL'
    EXACT = 'EXACT'
    NUMERIC_GREATER_THAN = 'NUMERIC_GREATER_THAN'
    NUMERIC_LESS_THAN = 'NUMERIC_LESS_THAN'
    NUMERIC_BETWEEN = 'NUMERIC_BETWEEN'
    IN_LIST = 'IN_LIST'


class MetricFilterOperator(Enum):
    """
    Different comparison type options.
    Enum value 	Description
    OPERATOR_UNSPECIFIED 	If the operator is not specified, it is treated as EQUAL.
    EQUAL 	Should the value of the metric be exactly equal to the comparison value.
    LESS_THAN 	Should the value of the metric be less than to the comparison value.
    GREATER_THAN 	Should the value of the metric be greater than to the comparison value.
    IS_MISSING 	Validates if the metric is missing. Doesn't take comparisonValue into account.
    """
    EQUAL = 'EQUAL'
    LESS_THAN = 'LESS_THAN'
    GREATER_THAN = 'GREATER_THAN'
    IS_MISSING = 'IS_MISSING'


class SegmentMetricFilterOperator(Enum):
    """

    """
    EQUAL = 'EQUAL'
    LESS_THAN = 'LESS_THAN'
    GREATER_THAN = 'GREATER_THAN'
    BETWEEN = 'BETWEEN'


class OrderType(Enum):
    """

    """
    VALUE = 'VALUE'
    DELTA = 'DELTA'
    SMART = 'SMART'
    HISTOGRAM_BUCKET = 'HISTOGRAM_BUCKET'
    DIMENSION_AS_INTEGER = 'DIMENSION_AS_INTEGER'


class SortOrder(Enum):
    """

    """
    ASCENDING = 'ASCENDING'
    DESCENDING = 'DESCENDING'


class Scope(Enum):
    """

    """
    PRODUCT = 'PRODUCT'
    HIT = 'HIT'
    SESSION = 'SESSION'
    USER = 'USER'


class MatchType(Enum):
    """

    """
    PRECEDES = 'PRECEDES'
    IMMEDIATELY_PRECEDES = 'IMMEDIATELY_PRECEDES'


class CohortType(Enum):
    """
    Only supported cohort type...
    """
    FIRST_VISIT_DATE = 'FIRST_VISIT_DATE'
