import requests
import concurrent.futures
import threading


def test_hello():
    thread_num = threading.current_thread().name
    print(f"Thread {thread_num}: Sending request")
    
    url = "http://localhost:8080/graphql"
    query = """
        query {
            hello
        }
    """
    response = requests.post(url, json={"query": query})
    
    print(f"Thread {thread_num}: Response - Status Code: {response.status_code}, Content: {response.content}")
    assert response.status_code == 200
    assert response.json() == {"data": {"hello": "world"}}


if __name__ == "__main__":
    # Number of requests and threads
    num_requests = 10000
    num_threads = 4

    # Create a thread pool executor
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        # Submit the test function to the executor multiple times
        futures = [executor.submit(test_hello) for _ in range(num_requests)]

        # Wait for all the test functions to complete
        concurrent.futures.wait(futures)
