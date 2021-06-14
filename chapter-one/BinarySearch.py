import time
## Binary Searhch
def binarySearch(a,i):
	low = 0 
	high = len(a)-1
	count = 0

	while low<=high:
		mid =round((low+high)/2)
		guess = a[mid]
		if guess == i:
			return f'Found at {mid} after {count} calculation '
		if guess >i:
			high = mid-1
			time.sleep(1)
			print(arr[low:high])
			count +=1
		else:
			low = mid +1
			time.sleep(1)

			print(arr[low:high])
			count +=1
	return None
			
if __name__ == '__main__':
	arr = list(range(64))

	print(binarySearch(arr,5))
