import { FileItem } from "@/entities";

export interface IComponentProps {
    files: FileItem[],
    isLoading: boolean,
}