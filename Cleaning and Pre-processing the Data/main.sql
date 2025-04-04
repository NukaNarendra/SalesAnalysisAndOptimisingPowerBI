create database optimising_power_bi;
select*from pizza;
select sum(quantity) as total_no_of_pizzas_sold from pizza;
select pizza_name,sum(total_price) as total_revenue from pizza group by pizza_name;
select pizza_name,sum(total_price) as total_top_revenue from pizza
group by pizza_name 
order by total_revenue desc limit 5;
select pizza_name,sum(total_price) as total_least_revenue from pizza
group by pizza_name 
order by total_revenue  limit 5;
select sum(distinct(order_id)) as total_orders from pizza;
select sum(quantity) / sum(distinct(order_id))  as average_pizzas_per_order from pizza;
select pizza_name,sum(quantity) as total_least_quantity from pizza 
group by pizza_name 
order by total_least_quantity limit 5;
select pizza_name,sum(quantity) as total_top_quantity from pizza 
group by pizza_name 
order by total_top_quantity  desc limit 5;
SELECT SUM(total_price) / sum(quantity)  as average_order_value FROM pizza ;  
select pizza_category ,sum(total_price) *100 /(select sum(total_price) from pizza) as pct from pizza group by pizza_category ;
desc pizza;
select str_to_date(order_date,'%d-%m-%Y') from pizza;