#include <thread>
#include <vector>

using namespace std;

void workerFunction() {
    while (true) {

    }
}

int main() {
    const int numThreads = thread::hardware_concurrency();
    vector<thread> threads;

    for (int i = 0; i < numThreads; ++i) {
        threads.emplace_back(workerFunction);
    }

    for (auto& thread : threads) {
        thread.join();
    }

    return 0;
}
