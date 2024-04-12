import math

def calculate_response_time(environment, N, W, S):
    if environment == "edge":
        return N + W + S
    elif environment == "cloud":
        return N + W + S
    else:
        raise ValueError("Please enter a valid environment!")

def calculate_rho(lambda_, max_capacity):
    return lambda_ / max_capacity   # Utilization Level

def calculate_delta_N(N_cloud, N_edge):
    return N_cloud - N_edge

def is_condition_met(delta_N, rho_edge, rho_cloud, K):
    delta_N_condition = delta_N < math.sqrt(2) / (1 - rho_edge)

    W_condition = (math.sqrt(2) / (1 - rho_edge) )-( math.sqrt(2) / ((1 - rho_cloud) * math.sqrt(K)))

    rho_condition = rho_edge > (1- (math.sqrt(2)/delta_N))*(1- (1/math.sqrt(K)))

    if delta_N_condition > W_condition and rho_condition:
        print("The Performance inversion occurred!")
    else:
        print("Edge offered good Latency.")

def response_time_edge(N_edge , rho_edge):
    return (N_edge) + (math.sqrt(2)/ (1-rho_edge))

def response_time_cloud(N_cloud, rho_cloud , K):
    return (N_cloud + (math.sqrt(2) /((1-rho_cloud) * math.sqrt(K) )))

def choose_deployment_setup():
    edge_servers = int(input("Enter the number of servers at each edge site (K): "))
    cloud_servers = int(input("Enter the number of servers at the cloud (K): "))
    n_edge = float(input("Enter the network latency of edge deployment (n_edge): "))
    n_cloud = float(input("Enter the network latency of cloud deployment (n_cloud): "))

    delta_n = n_cloud - n_edge
    cutoff_utilization = calculate_cutoff_utilization(delta_n)
    
    return edge_servers, cloud_servers, delta_n, cutoff_utilization

def choose_workload():
    max_request_rate = float(input("Enter the maximum request rate for the application (µ): "))
    request_rate_interval = input("Enter the request rate interval (e.g., 'from 6 to 12'): ")
    experiment_time_period = float(input("Enter the time period for each experiment (minutes): "))
    workload_distribution = input("Enter how request rate is divided between servers (equally or unequally): ")

    return max_request_rate, request_rate_interval, experiment_time_period, workload_distribution

def calculate_cutoff_utilization(delta_n):
    return math.sqrt(2) / (1 - delta_n)

def main():
    # Step 1: Choose a deployment setup
    edge_servers, cloud_servers, delta_n, cutoff_utilization = choose_deployment_setup()

    # Step 2: Choose a workload
    max_request_rate, request_rate_interval, experiment_time_period, workload_distribution = choose_workload()

    print("Edge Servers:", edge_servers)
    print("Cloud Servers:", cloud_servers)
    print("Δn (delta n):", delta_n)
    print("Cutoff Utilization:", cutoff_utilization)
    print("Maximum Request Rate:", max_request_rate)
    print("Request Rate Interval:", request_rate_interval)
    print("Experiment Time Period:", experiment_time_period)
    print("Workload Distribution:", workload_distribution)

if __name__ == "__main__":
    main()
