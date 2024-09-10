from app.enums import AppEnum


class ScanStatus(AppEnum):
    new = "New"
    in_progress = "InProgress"
    succeeded = "Succeeded"
    failed = "Failed"
