from osint.enums import AppEnum


class ScanStatus(AppEnum):
    new = "New"
    in_progress = "InProgress"
    succeeded = "Succeeded"
    failed = "Failed"
