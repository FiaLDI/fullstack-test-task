import { UiPack } from "@/shared";

export const Component = ({id}: {id: string}) => {

    const {
        Button,
    } = UiPack;

    return (
        <td className="text-nowrap">
            <Button
                as="a"
                href={`http://localhost:8000/files/${id}/download`}
                variant="outline-primary"
                size="sm"
            >
                Скачать
            </Button>
        </td>
    )
}