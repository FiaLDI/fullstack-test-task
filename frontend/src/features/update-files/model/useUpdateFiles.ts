import { AlertItem, FileItem } from "@/entities";

export const useUpdateFiles = () => {

    async function loadData(filesPagination: {max: number, skip: number}, alertsPagination: {max: number, skip: number}): Promise<{
        files: FileItem[];
        alerts: AlertItem[];
    }> {
        const [filesResponse, alertsResponse] = await Promise.all([
            fetch(`http://localhost:8000/files?max=${filesPagination.max}&skip=${filesPagination.skip}`, { cache: "no-store" }),
            fetch(`http://localhost:8000/alerts?max=${alertsPagination.max}&skip=${alertsPagination.skip}`, { cache: "no-store" }),
        ]);

        if (!filesResponse.ok || !alertsResponse.ok) {
            throw new Error("Не удалось загрузить данные");
        }

        const [filesData, alertsData] = await Promise.all([
            filesResponse.json() as Promise<FileItem[]>,
            alertsResponse.json() as Promise<AlertItem[]>,
        ]);

        return {
            files: filesData,
            alerts: alertsData,
        };
    }

    return { loadData };
};

