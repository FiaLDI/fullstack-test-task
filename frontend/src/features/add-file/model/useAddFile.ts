
import { FormEvent, useState } from "react";

export const useAddFile = () => {
    const [isSubmitting, setIsSubmitting] = useState(false);
    const [title, setTitle] = useState("");
    const [selectedFile, setSelectedFile] = useState<File | null>(null);

    async function submit() {
        if (!title.trim() || !selectedFile) {
            throw new Error("Укажите название и выберите файл");
        }

        setIsSubmitting(true);

        const formData = new FormData();
        formData.append("title", title.trim());
        formData.append("file", selectedFile);

        try {
            const response = await fetch(`http://localhost:8000/files`, {
                method: "POST",
                body: formData,
            });

            if (!response.ok) {
                throw new Error("Не удалось загрузить файл");
            }

            setTitle("");
            setSelectedFile(null);

        } finally {
            setIsSubmitting(false);
        }
    }

    return {
        submit,
        title,
        setTitle,
        setSelectedFile,
        isSubmitting
    };
};