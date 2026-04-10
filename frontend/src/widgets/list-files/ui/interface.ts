import { FileItem } from "@/entities";

export interface IComponentProps {
    files: FileItem[],
    isLoading: boolean,
    pagination: {max: number, skip: number};
    changePagination: (max, skip) => Promise<void>;
}