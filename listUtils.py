def list_product(lst):
        product = lst[0]

        for i in range(1, len(lst)):
                product *= lst[i]

        return product

def list_roll_left(lst, element):
        lst.pop(0)
        lst.append(element)

def list_roll_right(lst, element):
        lst.pop()
        lst.insert(0, element)

def delete_elems(list, elems):
	y = []
	y.extend(list)

	for elem in elems:
		if y.count(elem) > 0:
			y.remove(elem)

	return y
