package com.example.loginform;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    EditText username, password;
    Button login_btn;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        username = findViewById(R.id.etname);
        password = findViewById(R.id.etpwd);
        login_btn = findViewById(R.id.login);
    }

    public void onClick(View view) {
        String s1 = username.getText().toString();
        String s2 = password.getText().toString();
        if(s1.equals("uname") && s2.equals("pswrd"))
        {
            Toast.makeText(this, "Login Successfully!!!", Toast.LENGTH_LONG).show();
        }
        else
        {
            Toast.makeText(this, "Invalid Username and Password!!!", Toast.LENGTH_LONG).show();
        }
    }
}