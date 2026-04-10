
from pathlib import Path
from src.domain.files.service import FilesDomainService


class FileProcessingHandler:

    def __init__(self, service: FilesDomainService):
        self.service = service

    async def scan_file(self, file_id: str):
        file = await self.service.get_file(file_id)

        reasons = []
        ext = Path(file.original_name).suffix.lower()

        if ext in {".exe", ".bat", ".cmd", ".sh", ".js"}:
            reasons.append(f"suspicious extension {ext}")

        if file.size > 10 * 1024 * 1024:
            reasons.append("file is larger than 10 MB")

        file.mark_as_scanned(
            "suspicious" if reasons else "clean",
            ", ".join(reasons) if reasons else "no threats found",
        )

        await self.service.create_alert(
            file.id,
            "warning" if reasons else "info",
            file.scan_details,
        )

        return file


class MetadataHandler:

    def __init__(self, service: FilesDomainService):
        self.service = service

    async def extract_metadata(self, file_id: str, storage_dir: Path):
        file = await self.service.get_file(file_id)

        path = storage_dir / file.stored_name
        if not path.exists():
            await self.service.create_alert(file.id, "critical", "file missing")
            return

        metadata = {
            "extension": Path(file.original_name).suffix.lower(),
            "size_bytes": file.size,
            "mime_type": file.mime_type,
        }

        file.metadata_json = metadata

        return file
