import { AlertItem } from "@/entities";

export interface IComponentProps {
    alerts: AlertItem[];
    isLoading: boolean;
    pagination: {max: number, skip: number};
    changePagination: (max, skip) => Promise<void>;
}
