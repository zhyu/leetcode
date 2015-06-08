select a.Id from Weather as a join Weather as b on a.Date=date_add(b.Date, interval 1 day) where a.Temperature>b.Temperature;
