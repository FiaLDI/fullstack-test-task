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
    const [paginationFiles, setPaginationFiles] = useState<{max: number, skip: number}>({
        max: 2,
        skip: 0,
    })
    const [paginationAlerts, setPaginationAlerts] = useState<{max: number, skip: number}>({
        max: 2,
        skip: 0,
    })

    const { loadData } = useUpdateFiles();
    const addFile = useAddFile();

    const handleLoad = async () => {
        setIsLoading(true);
        setErrorMessage(null);

        try {
            const { files, alerts } = await loadData(
                paginationFiles, 
                paginationAlerts
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
            await addFile.submit();

            setShowModal(false);
            await handleLoad();
        } catch (error) {
            setErrorMessage(error.message);
        }
    };

    const handleChangePaginationFiles = async(max, skip) => {
        setPaginationFiles({max, skip})
    }

    const handleChangePaginationAlerts = async(max, skip) => {
        setPaginationAlerts({max, skip})
    }

    useEffect(()=>{
        handleLoad()
    }, [])

    useEffect(()=>{
        handleLoad()
    }, [paginationFiles.max, paginationFiles.skip, paginationAlerts.max, paginationAlerts.skip])

    return {
        files,
        alerts,
        showModal,
        setShowModal,
        errorMessage,
        setErrorMessage,
        isLoading,
        handleLoad,
        handleSubmit,
        addFile,
        handleChangePaginationFiles,
        handleChangePaginationAlerts,
        paginationFiles,
        paginationAlerts
    }
}