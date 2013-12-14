#!/bin/bash
echo "Generating thrift libraries"
thrift --gen py stringstore.thrift


