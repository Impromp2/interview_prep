#!/usr/bin/env ruby

require 'soda/client'

client = SODA::Client.new({:domain => "data.cityofnewyork.us", :app_token => "cuug8Z8Xu4xrx8BW7Kv1F2Knm"})

results = client.get("d9fw-zp4j", :$limit => 1000, :sub_subindustry => "Pizza")

puts "Got #{results.count} results:"

pizzas = {}

results.each do |x|
	puts "#{x[:company_name]}"
end