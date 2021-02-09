(
    {"environment/env_name": "PongNoFrameskip-v4",
            "n_envs": 1,
            "max_episode_steps": 15000,
            "discount_factor": 0.99,
            "epsilon_greedy_max": 0.99,
            "epsilon_greedy_min": 0.01,
            "epsilon_min_epoch": [100000,200000],
            "replay_buffer_size": [100000],
            "n_batches": 32,
            "use_duelling": [False,True],
            "use_double": [False,True],
            "lr": [1e-4,3e-5,1e-5],
            "n_evaluation_processes": 4,
            "verbose": True,
            "n_evaluation_envs": 4,
            "time_limit": 28800,
            "env_seed": 48,
            "clip_grad": [2.0],
            "learner_device": "cuda",

            "as_fast_as_possible":[True,False],

            "update_target_hard":[True],
            "update_target_epoch":1000,
            "update_target_tau": 0.005,

            "logdir":"/checkpoint/denoyer/pong",
            "save_every":100,
    }
,
    [
        {
            "initial_buffer_epochs": 2500,
            "qvalue_epochs": 1,
            "batch_timesteps": 1,
            "n_processes": 4,
            "buffer/alpha":0.0,
            "buffer/beta":0.0,
        }
        ,
        {
            "initial_buffer_epochs": 2500,
            "qvalue_epochs": 1,
            "batch_timesteps": 1,
            "n_processes": 4,
            "buffer/alpha":0.4,
            "buffer/beta":0.6,
        }
        ,
        {
            "initial_buffer_epochs": 600,
            "qvalue_epochs": 4,
            "batch_timesteps": 4,
            "n_processes": 4,
            "buffer/alpha":0.0,
            "buffer/beta":0.0,
        }
        ,
        {
            "initial_buffer_epochs": 600,
            "qvalue_epochs": 4,
            "batch_timesteps": 4,
            "n_processes": 4,
            "buffer/alpha":0.6,
            "buffer/beta":0.4,
        }
        ,
        {
            "initial_buffer_epochs": 120,
            "qvalue_epochs": 1,
            "batch_timesteps": 20,
            "n_processes": 4,
            "buffer/alpha":0.0,
            "buffer/beta":0.0,
        },
        {
            "initial_buffer_epochs": 120,
            "qvalue_epochs": 1,
            "batch_timesteps": 20,
            "n_processes": 4,
            "buffer/alpha":0.6,
            "buffer/beta":0.4,
        },
    ]
)