drop table if exists prototyping.global_superstore_prepped
;
create table prototyping.global_superstore_prepped
as 
SELECT "index" as id
		, category
		, city
		, country
		, customer_name
		, market
		, customer_id
		, to_date(order_date,'dd/mm/yyyy') as order_date
		, order_id
		, order_priority
		, product_id
		, product_name
		, region
		, row_id
		, segment
		, to_date(ship_date,'dd/mm/yyyy') as ship_date
		, ship_mode
		, state
		, sub_category
		, discount
		, replace(profit,',','')::float as profit 
		, quantity
		, replace(sales,',','')::float as sales 
		, shipping_cost
FROM prototyping.global_superstore
;
grant all on prototyping.global_superstore_prepped to grp_dev
;
alter table prototyping.global_superstore_prepped owner to grp_dev 
;