func hasDuplicate(nums []int) bool {
    hashset := make(map[int]bool)
    for _, n := range nums{
        if _, exists:= hashset[n]; exists{
            return true
        }
        hashset[n] = true
    }
    return false
    
    
}
