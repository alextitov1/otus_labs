## SLO (Service level objectives)
* 99% of GETs requests will complete in less than 100ms (average over 1 hour)
* 90% of add POST requests will complete in less than 200ms
* 99% of update POST requests will complete and not fail



## SLI (Service level indicators)
* Average GET requests completion time over 1 hour
* Complete add POST requests *100 / valid add POST requests
* Good update POST requests * 100 / all update POST requests


## Error budget
The service is design to handle 100 update POST requests per second. However if the number of request exceeds the threshold, SLOs can be breached.
