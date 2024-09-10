from app.enums import AppEnum


class ScanStatus(AppEnum):
    created = "Created"
    in_progress = "In Progress"
    succeeded = "Succeeded"
    failed = "Failed"
