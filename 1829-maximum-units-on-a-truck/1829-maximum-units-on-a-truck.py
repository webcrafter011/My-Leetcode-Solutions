class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: x[1], reverse=True)

        total_boxes = units = 0
        for box in boxTypes:
            if total_boxes + box[0] < truckSize:
                total_boxes += box[0]
                units += box[1] * box[0]
            else:
                units += (truckSize - total_boxes) * box[1]
                break
        
        return units