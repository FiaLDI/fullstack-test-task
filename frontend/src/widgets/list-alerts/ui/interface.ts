import { AlertItem } from "@/entities";

export interface IComponentProps {
    alerts: AlertItem[], 
    isLoading: boolean;
}
