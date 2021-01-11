# Tests

# Description of metrics
https://www.joedog.org/siege-manual/

## siege -d1 -c10 -r10 http://localhost:8080/main
    "transactions":                          100,
    "availability":                       100.00,
    "elapsed_time":                        11.59,
    "data_transferred":                     0.02,
    "response_time":                        0.42,
    "transaction_rate":                     8.63,
    "throughput":                           0.00,
    "concurrency":                          3.60,
    "successful_transactions":               100,
    "failed_transactions":                     0,
    "longest_transaction":                  1.30,
    "shortest_transaction":                 0.05

## siege -d1 -c25 -r10 http://localhost:8080/main
    "transactions":                          250,
    "availability":                       100.00,
    "elapsed_time":                        17.52,
    "data_transferred":                     0.05,
    "response_time":                        0.97,
    "transaction_rate":                    14.27,
    "throughput":                           0.00,
    "concurrency":                         13.87,
    "successful_transactions":               250,
    "failed_transactions":                     0,
    "longest_transaction":                  1.83,
    "shortest_transaction":                 0.09

## siege -d1 -c50 -r10 http://localhost:8080/main
    "transactions":                          500,
    "availability":                       100.00,
    "elapsed_time":                        36.02,
    "data_transferred":                     0.10,
    "response_time":                        2.82,
    "transaction_rate":                    13.88,
    "throughput":                           0.00,
    "concurrency":                         39.13,
    "successful_transactions":               500,
    "failed_transactions":                     0,
    "longest_transaction":                  4.06,
    "shortest_transaction":                 0.08

##siege -d1 -c100 -r10 http://localhost:8080/main
    "transactions":                         1000,
    "availability":                       100.00,
    "elapsed_time":                        82.67,
    "data_transferred":                     0.21,
    "response_time":                        7.33,
    "transaction_rate":                    12.10,
    "throughput":                           0.00,
    "concurrency":                         88.61,
    "successful_transactions":              1000,
    "failed_transactions":                     0,
    "longest_transaction":                 11.07,
    "shortest_transaction":                 0.32

## siege -d1 -c255 -r10 http://localhost:8080/main
### without cache
    "transactions":                         2445,
    "availability":                        95.88,
    "elapsed_time":                       230.41,
    "data_transferred":                     0.50,
    "response_time":                       14.61,
    "transaction_rate":                    10.61,
    "throughput":                           0.00,
    "concurrency":                        155.02,
    "successful_transactions":              2445,
    "failed_transactions":                   105,
    "longest_transaction":                 78.16,
    "shortest_transaction":                 0.08

### with cache 20 sec
    "transactions":                         2550,
    "availability":                       100.00,
    "elapsed_time":                        37.50,
    "data_transferred":                     0.52,
    "response_time":                        2.01,
    "transaction_rate":                    68.00,
    "throughput":                           0.01,
    "concurrency":                        136.70,
    "successful_transactions":              2550,
    "failed_transactions":                     0,
    "longest_transaction":                 29.20,
    "shortest_transaction":                 0.01



## Conclusions
 - transaction_rate is 8 - 14 - 12 - 10. So the optimal speed is for 25 concurent users
 - When concurency = 255, we lose 0,4% of transactions
 - Longest transaction: 1,3 - 1,83 - 4,06 - 11,07 - 78,16
 - Response time: 0,42 - 0,97 - 2,82 - 7,33 - 14,61
 - Cache give total increasing if productivity - 68 against 10 for 255 concurent processes