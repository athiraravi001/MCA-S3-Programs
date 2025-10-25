package com.example.sqlitedatabase;

import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    EditText ename, eplace, eid;
    Button bsubmit, bsel, bup, bdel, bclr;
    TextView tid, tname, tplace;
    SQLiteDatabase db;
    AlertDialog.Builder builder;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        ename = findViewById(R.id.ET_name);
        eplace = findViewById(R.id.ET_place);
        eid = findViewById(R.id.ET_id);

        bsubmit = findViewById(R.id.B_submit);
        bsel = findViewById(R.id.B_sel);
        bup = findViewById(R.id.B_update);
        bdel = findViewById(R.id.B_delete);
        bclr = findViewById(R.id.B_clear);

        //tid = findViewById(R.id.T_id);
        //tname = findViewById(R.id.T_name);
        //tplace = findViewById(R.id.T_place);

        builder = new AlertDialog.Builder(this);

        try {
            db = openOrCreateDatabase("empdb", MODE_PRIVATE, null);
            db.execSQL("CREATE TABLE IF NOT EXISTS employee(id INTEGER PRIMARY KEY, name TEXT, place TEXT)");
            Toast.makeText(getApplicationContext(), "Created Successfully", Toast.LENGTH_SHORT).show();
        } catch(Exception e) {
            // table already exists or other exception
        }

        // Insert Button
        bsubmit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                try {
                    db.execSQL("INSERT INTO employee VALUES (" +
                            eid.getText().toString() + ",'" +
                            ename.getText().toString() + "','" +
                            eplace.getText().toString() + "')");
                    Toast.makeText(getApplicationContext(), "Record Inserted Successfully", Toast.LENGTH_SHORT).show();
                } catch (Exception e) {
                    Toast.makeText(getApplicationContext(), "Error in Data", Toast.LENGTH_SHORT).show();
                }
            }
        });

        // Clear fields initially
        bclr.callOnClick();

        // Select Button
        bsel.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Cursor c = db.rawQuery("SELECT * FROM employee", null);
                if (c.getCount() == 0) {
                    Toast.makeText(getApplicationContext(), "No such record", Toast.LENGTH_SHORT).show();
                } else {
                    StringBuffer b = new StringBuffer();
                    while (c.moveToNext()) {
                        b.append("Id: " + c.getString(0) + "\n");
                        b.append("Name: " + c.getString(1) + "\n");
                        b.append("Place: " + c.getString(2) + "\n");
                    }
                    Toast.makeText(getApplicationContext(), b.toString(), Toast.LENGTH_LONG).show();
                    builder.setMessage(b.toString());
                    AlertDialog alert = builder.create();
                    alert.setTitle("Employee Data");
                    alert.show();
                }
            }
        });

        // Update Button
        bup.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                db.execSQL("UPDATE employee SET name='" + ename.getText().toString() +
                        "', place='" + eplace.getText().toString() +
                        "' WHERE id=" + eid.getText().toString());
                Toast.makeText(getApplicationContext(), "Updated....", Toast.LENGTH_SHORT).show();
            }
        });

        // Delete Button
        bdel.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                db.execSQL("DELETE FROM employee WHERE id=" + eid.getText().toString());
                Toast.makeText(getApplicationContext(), "Item Deleted", Toast.LENGTH_SHORT).show();
            }
        });

        // Clear Button
        bclr.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                eid.setText("");
                ename.setText("");
                eplace.setText("");
            }
        });

        // Clear fields initially
        bclr.callOnClick();
    }
}