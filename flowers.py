
def find_min_cost(N, K, costs):
    # N = Total number of flowers to be purchased
    # K = Total number of people
    # costs = cost of each flower

    costs = sorted(costs, reverse = True)
    total_cost = 0
    num_flowers_per_person = []
    for i in range(0, K):
	num_flowers_per_person.append(0)
    
    cost_index = 0

    while True:
	for index in range(0, len(num_flowers_per_person)):
	    total_cost = total_cost + (num_flowers_per_person[index] + 1) * costs[cost_index]
	    cost_index = cost_index + 1
	    num_flowers_per_person[index] += 1

	    if sum(num_flowers_per_person) == N:
		return total_cost

if __name__ == '__main__':
    print find_min_cost(N = 3, K = 3, costs = [2, 5, 6])
    print find_min_cost(N = 3, K = 2, costs = [2, 5, 6])