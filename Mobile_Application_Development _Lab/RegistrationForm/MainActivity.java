package com.example.registrationform;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.EditText;
import android.widget.RadioButton;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    // UI elements
    EditText name, email, dob, pwd;
    RadioButton btMale, btFemale, btOther;
    Button submit;
    CheckBox check;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Initialize views
        name = findViewById(R.id.rname);
        email = findViewById(R.id.remail);
        dob = findViewById(R.id.rdob);
        pwd = findViewById(R.id.rpswrd);
        submit = findViewById(R.id.rsubmit);
        btMale = findViewById(R.id.rmale);
        btFemale = findViewById(R.id.rfemale);
        btOther = findViewById(R.id.rother);
        check = findViewById(R.id.rcheck);

        // Set click listener for register button
        submit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (checkAllFields()) {
                    Toast.makeText(MainActivity.this, "Registered Successfully!", Toast.LENGTH_SHORT).show();
                }
            }
        });
    }

    private boolean checkAllFields() {
        // Name validation
        if (name.getText().toString().trim().isEmpty()) {
            name.setError("Name is required");
            return false;
        }

        // Email validation
        if (email.getText().toString().trim().isEmpty()) {
            email.setError("Email is required");
            return false;
        } else {
            String e_mail = email.getText().toString();
            String checkemail = "[a-zA-Z0-9._-]+@[a-z]+\\.+[a-z]+";
            if (!e_mail.matches(checkemail)) {
                email.setError("Invalid Email");
                return false;
            }
        }

        // Password validation
        if (pwd.getText().toString().trim().isEmpty()) {
            pwd.setError("Password is required");
            return false;
        } else if (pwd.getText().toString().length() < 8) {
            pwd.setError("Password must be minimum 8 characters");
            return false;
        }


        // Gender validation
        if (!btMale.isChecked() && !btFemale.isChecked() && !btOther.isChecked()) {
            Toast.makeText(this, "Please select gender", Toast.LENGTH_SHORT).show();
            return false;
        }

        // Checkbox validation
        if (!check.isChecked()) {
            check.setError("Please agree to Privacy Policy");
            check.requestFocus();
            return false;
        }

        return true; // All fields are valid
    }
}
