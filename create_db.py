import sqlite3


if __name__ == "__main__":
    print('ok')
    conn = sqlite3.connect('developpers.db')
    c = conn.cursor()

    create_developpers_query = """
        CREATE TABLE developpers (
            first_name text,
            last_name text,
            techno text,
            experience integer
        )
    """
    
    insert_developpers_qry = """
        INSERT INTO developpers 
        VALUES ('alessio', 'rea', 'node.js', 0),
        VALUES ('mathieux', 'bordet', 'react', 10),
        VALUES ('julien', 'ducros', 'java', 5)
    """

    c.execute(insert_developpers_qry)
    c.execute(create_table_query)
    conn.commit()

    create_technos_query = """
        CREATE TABLE technos (
            name text,
            type text
        )
    """

    insert_technos_qry = """
        INSERT INTO technos 
        VALUES ('node.js', 'web'),
        VALUES ('react native', 'mobile'),
        VALUES ('jave', 'web'),
        VALUES ('swift', 'mobile')
    """

    c.execute(create_technos_query)
    c.execute(insert_technos_qry)
    conn.commit()

 
    conn.close()

    #c.execute("SELECT * FROM addresses WHERE oid = " + record_id)


    # c.execute("""UPDATE addresses SET
	# 	first_name = :first,
	# 	last_name = :last,
	# 	address = :address,
	# 	city = :city,
	# 	state = :state,
	# 	zipcode = :zipcode 

	# 	WHERE oid = :oid""",
	# 	{
	# 	'first': f_name_editor.get(),
	# 	'last': l_name_editor.get(),
	# 	'address': address_editor.get(),
	# 	'city': city_editor.get(),
	# 	'state': state_editor.get(),
	# 	'zipcode': zipcode_editor.get(),
	# 	'oid': record_id
	# 	})

    #c.execute("DELETE from addresses WHERE oid = " + delete_box.get())

    
