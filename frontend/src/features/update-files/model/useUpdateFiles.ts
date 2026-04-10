import { AlertItem, FileItem } from "@/entities";

export const useUpdateFiles = () => {

    async function loadData(skip: number, max: number): Promise<{
        files: FileItem[];
        alerts: AlertItem[];
    }> {
        const [filesResponse, alertsResponse] = await Promise.all([
            fetch(`http://localhost:8000/files?max=${max}&skip=${skip}`, { cache: "no-store" }),
            fetch(`http://localhost:8000/alerts?max=${max}&skip=${skip}`, { cache: "no-store" }),
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

