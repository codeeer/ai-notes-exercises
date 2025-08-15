package com.example.sample.service;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.example.sample.entity.User;
import com.example.sample.repository.UserRepository;

@Service
public class UserService {
    
    @Autowired
    private UserRepository userRepository;
    
    // Tüm kullanıcıları getir
    public List<User> getAllUsers() {
        return userRepository.findAll();
    }
    
    // ID ile kullanıcı getir
    public Optional<User> getUserById(Long id) {
        return userRepository.findById(id);
    }
    
    // Email ile kullanıcı getir
    public Optional<User> getUserByEmail(String email) {
        return userRepository.findByEmail(email);
    }
    
    // İsimde arama yap
    public List<User> searchUsersByName(String name) {
        return userRepository.findByNameContainingIgnoreCase(name);
    }
    
    // Yeni kullanıcı oluştur
    public User createUser(User user) {
        return userRepository.save(user);
    }
    
    // Kullanıcı güncelle
    public User updateUser(Long id, User userDetails) {
        Optional<User> userOptional = userRepository.findById(id);
        if (userOptional.isPresent()) {
            User user = userOptional.get();
            user.setName(userDetails.getName());
            user.setEmail(userDetails.getEmail());
            return userRepository.save(user);
        }
        return null;
    }
    
    // Kullanıcı sil
    public boolean deleteUser(Long id) {
        if (userRepository.existsById(id)) {
            userRepository.deleteById(id);
            return true;
        }
        return false;
    }
    
    // Kullanıcı sayısını getir
    public long getUserCount() {
        return userRepository.count();
    }
}
