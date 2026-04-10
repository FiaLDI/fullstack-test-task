
import asyncio

from test_files import test_create_file, test_list_files
from test_service import test_service_create_get


async def main():
    print("Running tests...\n")

    await test_create_file()
    print("test_create_file done")

    await test_list_files()
    print("test_list_files done")

    await test_service_create_get()
    print("test_service_create_get done")

    print("\nALL TESTS PASSED ")


if __name__ == "__main__":
    asyncio.run(main())
    