import { useChangePagination } from "../model/useChangePagination";

export const Component = ({pagination, handleChange}) => {

    const {limits, 
        changeMax,
        changeSkip} = useChangePagination(pagination, handleChange);

    return (
        <div className="d-flex gap-5">
            <button onClick={()=>changeSkip(pagination.skip - pagination.max)}>Prev</button>
            <button onClick={()=>changeSkip(pagination.skip + pagination.max)}>Next</button>

            <div className="">Limit:</div>
            <div className="">{limits.map(val => {

                return (
                    <button onClick={() =>changeMax(val)}>{val}</button>
                )
            })}</div>
        </div>
    )
}