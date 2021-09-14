from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.compute import Server


with Diagram(name="Flask service", show=False):
    server=Server("App1")