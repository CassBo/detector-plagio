def merge_sort(arr, key=lambda x: x, reverse=False):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half, key, reverse)
        merge_sort(right_half, key, reverse)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if (key(left_half[i]) < key(right_half[j]) and not reverse) or \
               (key(left_half[i]) > key(right_half[j]) and reverse):
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr  # Asegúrate de devolver la lista ordenada