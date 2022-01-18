#### 1. User-defined variables (prefixed with @): 
select @var_name or set @var_name = value or select @var_name := value, null with be assigned if not set. 

#### 2. Local Variables with Function together
CREATE FUNCTION function_name(parameter parameter_datatype) 
RETURNS parameter_datatype

BEGIN

   DECLARE var_name datatype unsigned DEFAULT value (if no value assigned as null) 

   executable_section (select * ...)

END;

CALL function_name(parameter)
