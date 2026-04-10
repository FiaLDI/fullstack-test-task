"use client"
import { useState, useEffect } from "react";

import { AlertItem, FileItem } from "@/entities";
import { useUpdateFiles } from "@/features/update-files";
import { useAddFile } from "@/features/add-file";

export const usePage = () => {

    const [files, setFiles] = useState<FileItem[]>([]);
    const [alerts, setAlerts] = useState<AlertItem[]>([]);
    const [showModal, setShowModal] = useState(false);
    const [errorMessage, setErrorMessage] = useState<string | null>(null);
    const [isLoading, setIsLoading] = useState(false);
    const [pagination, SetPagination] = useState<{max: number, skip: number}>({
        max: 2,
        skip: 1,
    })

    const { loadData } = useUpdateFiles();
    const { submit } = useAddFile();

    const handleLoad = async () => {
        setIsLoading(true);
        setErrorMessage(null);

        try {
            const { files, alerts } = await loadData(
                pagination.skip, 
                pagination.max
            );

            setFiles(files);
            setAlerts(alerts);
        } catch (error) {
            setErrorMessage(
                error instanceof Error ? error.message : "Произошла ошибка"
            );
        } finally {
            setIsLoading(false);
        }
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            await submit();

            setShowModal(false);
            await handleLoad();
        } catch (error) {
            setErrorMessage(error.message);
        }
    };

    useEffect(()=>{
        handleLoad()
    }, [])

    return {
        files,
        alerts,
        showModal,
        setShowModal,
        errorMessage,
        setErrorMessage,
        isLoading,
        handleLoad,
        handleSubmit
    }
}