import collections


class InventoryAllocator:
    def produceShipment(orderItems, warehouses):
        cheapestShipment = collections.defaultdict(dict)

        for item in orderItems:
            inventoryMatch = False
            itemCount = orderItems[item]

            for warehouse in warehouses:
                warehouseName = warehouse["name"]
                inventory = warehouse["inventory"]

                if item in inventory:
                    inventoryItemAmount = inventory[item]
                    amountFromWarehouse = 0

                    if inventoryItemAmount < itemCount:
                        amountFromWarehouse = inventoryItemAmount
                        itemCount -= inventoryItemAmount
                    else:
                        amountFromWarehouse = itemCount
                        itemCount = 0
                        inventoryMatch = True

                    if item in cheapestShipment[warehouseName]:
                        cheapestShipment[warehouseName][item] += amountFromWarehouse
                    else:
                        cheapestShipment[warehouseName][item] = amountFromWarehouse

                if inventoryMatch:
                    break

            # Not sure if the question wanted to return [] if ONE item wasn't fulfilled, if so, uncomment the 2 lines below
            # if not inventoryMatch:
            #     return []

        return [{item: cheapestShipment[item]} for item in cheapestShipment]



#Input
order = { "apple": 10, "banana": 4 }
warehouses = [{ "name": "owd", "inventory": { "apple": 5, "banana" : 2 } }, { "name": "dm", "inventory": { "apple": 5 }}]

#Run class function
cheapestShipment = InventoryAllocator.produceShipment(order, warehouses)
#Prints output
print(cheapestShipment)



















