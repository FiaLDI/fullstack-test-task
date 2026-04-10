
export const useChangePagination = (pagination, handleChange) => {

    const limits = [2, 4, 6, 8];

    const changeMax = (val: number) => {
        handleChange(val, 0)
    }

    const changeSkip = (val: number) => {
        if (val >= 0)
            handleChange(pagination.max, val)
    }

    return {
        limits,
        changeMax,
        changeSkip
    }
}