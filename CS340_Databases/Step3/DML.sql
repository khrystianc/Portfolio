-- Get all Classes to list on Classes page
SELECT * FROM Classes;
-- Get all Teachers to list on Teachers page
SELECT * FROM Teachers;
-- Get all Children to list on Children page
SELECT * FROM Children;
-- Get all Learning Resources to list on Learning Resource page
SELECT * FROM Learning_Resources;
-- Get all Intersections to list on Intersections page
SELECT * FROM Class_Learning_Resource_Intersections;
-- Get all Costs to list on Class Costs page
SELECT * FROM Class_Costs;

-- Insert Child
INSERT INTO Children (First_Name, Last_Name, Age, Class_ID, Tuition_Is_Paid, Favorite_Learning_Resource_ID)
VALUES (:fnameInput, :lnameInput, ageInput, :class_id_from_dropdown_Input, :tuition_status_from_dropdown_Input, :learning_resource_id_from_dropdown_Input)
-- Get Child
SELECT Child_ID, First_Name, Last_Name, Age FROM Children
WHERE Child_ID = :child_ID_selected_from_browse_children_page
-- Update Child
UPDATE Children SET First_Name = :fnameInput, Last_Name= :lnameInput, Age= :ageInput 
WHERE Child_ID = :child_ID_from_the_update_form
-- Delete Child
DELETE FROM Children WHERE Child_ID = :child_ID_selected_from_browse_children_page

-- Insert Teacher
INSERT INTO Teacher (First_Name, Last_Name, Class_ID)
VALUES (:fnameInput, :lnameInput, :class_id_from_dropdown_Input)
-- Get Teacher
SELECT Teacher_ID, First_Name, Last_Name FROM Teacher
WHERE Teacher_ID = :teacher_ID_selected_from_browse_teachers_page
-- Update Teacher
UPDATE Teacher SET First_Name = :fnameInput, Last_Name= :lnameInput 
WHERE Teacher_ID = :teacher_ID_from_the_update_form
-- Delete Teacher
DELETE FROM Teacher WHERE Teacher_ID = :teacher_ID_selected_from_browse_teachers_page

-- Get Class Costs
SELECT Class_Cost_ID, Age_Range, Cost_Per_Child FROM Class_Costs
WHERE Class_Cost_ID = :cost_ID_selected_from_browse_costs_page
-- Update Class costs
UPDATE Class_Costs SET Age_Range = :ageInput, Cost_Per_Child= :costInput 
WHERE Class_Cost_ID = :cost_ID_selected_from_browse_costs_page

-- Insert Class
INSERT INTO Classes (Class_Name, Class_Size, Class_Cost_ID)
VALUES (:className, :classSize, :cost_ID_selected_from_dropdown_Input)
-- Update Class
UPDATE Classes SET Class_Name = :cnameInput, Class_Size= :csizeInput 
WHERE Class_ID = :class_ID_from_the_update_form

-- Insert Learning Resource
INSERT INTO Learning_Resources (Learning_Resource_Name, Price, On_Hand_Quantity, Renewal_Status, Learning_Resource_ID)
VALUES (:resourceName, :resourcePrice, :ohQuantity, :renewalStatus, :resource_ID_selected_from_dropdown_Input)
-- Update Learning Resource
UPDATE Learning_Resources SET Learning_Resource_Name = :lrnameInput, Price= :priceInput, On_Hand_Quantity= :quantityInput, Renewal_Status= rstatusInput
WHERE Learning_Resource_ID = :resource_ID_from_the_update_form


-- Insert Intersection??


-- Search/Dynamic Children

