/*
Develop an application to create 2 activities.
First Activity for create a login page and give proper validations. If login successfully navigate to second activity.
Second Activity for display any 2 logos. When clicking on each logo display its details.
*/

package com.example.logintologointerface;

import androidx.appcompat.app.AppCompatActivity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    EditText etname, etpwd;
    Button login;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        etname = findViewById(R.id.etname);
        etpwd = findViewById(R.id.etpwd);
        login = findViewById(R.id.login);
    }

    public void onClick(View view) {
        String username = etname.getText().toString();
        String password = etpwd.getText().toString();

        if (username.isEmpty() || password.isEmpty())
        {
            Toast.makeText(MainActivity.this, "Please enter both Username and Password.", Toast.LENGTH_SHORT).show();
        }
        else if (username.equals("uname") && password.equals("pswrd"))
        {
            Toast.makeText(MainActivity.this, "Login Successful! " + username, Toast.LENGTH_SHORT).show();
            Intent i = new Intent(MainActivity.this, MainActivity2.class);
            startActivity(i);
        }
        else
        {
            Toast.makeText(MainActivity.this, "Invalid Username or Password!", Toast.LENGTH_SHORT).show();
        }
    }
}