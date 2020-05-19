from dataclasses import dataclass


@dataclass
class HistoricalDataParams:
    end_date_time: str
    duration_str: str
    bar_size_setting: str
    what_to_show: str
    use_rth: int
    format_date: int
    keep_up_to_date: bool
